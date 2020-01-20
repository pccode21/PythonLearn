import requests
import time
import re
from pyquery import PyQuery
import pymysql


url_time = time.strftime('%Y%m%d%H%M%S')
team_list_url = 'http://zq.win007.com/jsData/matchResult/2019-2020/s36.js?version='+url_time
player_list_url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/'
player_info_url = 'http://zq.win007.com/cn/team/player.aspx?'
headers = {
            'Host': 'zq.win007.com',
            'Referer': 'http://zq.win007.com/cn/League/2019-2020/36.html',  # 需要加入跳转网页
            'Connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
            }
sql_insert = "insert into football_player(SimpName, EngName, TradName, price, birthday, weight, height, IdioFoot, nationality, contract) values (%(jiantiming)s, %(yingwenming)s, %(fantiming)s, %(yujishenjia)s, %(shengri)s, %(tizhong)s, %(shengao)s, %(guanyongjiao)s, %(guoji)s, %(hetongjiezhiqi)s)"


def connect():
    """
    数据库连接，请使用自己的MySQL的配置
    :return:
    """
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='Lxd05230708',
                           database='spider',
                           charset='utf8mb4')

    # 获取操作游标
    cursor = conn.cursor()
    return {"conn": conn, "cursor": cursor}


connection = connect()
conn, cursor = connection['conn'], connection['cursor']


def get_teams_list(teamListURL):
    response = requests.get(url=team_list_url, headers=headers)
    pattern = 'var arrTeam =(.*?);'
    res = re.search(pattern, response.text).group(1)  # group(1) 列出第一个括号匹配部分
    res = eval(res)  # eval() 函数用来执行一个字符串表达式，并返回表达式的值
    team_id_list = []
    for i in res:
        team_id = i[0]
        team_id_list.append(team_id)
    return team_id_list


time.sleep(2)


def get_player_list(list, playerListURL):
    for i in list:
        i = 19  # 由于批量爬取出错，只能一队队爬取,19代表阿森纳
        time.sleep(2)
        headers = {
                    'Referer': 'http://zq.win007.com/cn/team/PlayerData/{}.html'.format(i),
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        url = player_list_url + 'tdl{}.js?version={}'.format(i, url_time)
        s = requests.session()
        s.keep_alive = False
        response = requests.get(url=url, headers=headers)
        pattern = 'var lineupDetail=(.*?);'
        res = re.search(pattern, response.text).group(1)
        res = eval(res)
        player_id_list = []
        time.sleep(2)
        for i in res:
            try:
                player_id = i[0]
                player_id_list.append(player_id)
            except:
                continue
        return player_id_list


def get_player_info(player_list, playInfoURL):
    for player in player_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
        try:
            url = playInfoURL + 'PlayerID={}&TeamID=19'.format(player)  # 由于批量爬取出错，只能一队队爬取，19代表阿森纳
            response = requests.get(url, headers=headers)
            doc = PyQuery(response.text)
            table = doc('.tdlink')
            insert_data = {
                # 简体名
                'jiantiming': table('tr:nth-child(1) > td:nth-child(3) > strong').text(),
                # 英文名
                'yingwenming': table('tr:nth-child(1) > td:nth-child(5) > span > strong').text(),
                # 繁体名
                'fantiming': table('tr:nth-child(2) > td:nth-child(2) > span > strong').text(),
                # 预计身价
                'yujishenjia': table('tr:nth-child(2) > td:nth-child(4) > strong > span > strong').text(),
                # 生日
                'shengri': table('tr:nth-child(3) > td:nth-child(2) > strong > span > strong').text(),
                # 体重
                'tizhong': table('tr:nth-child(3) > td:nth-child(4) > strong').text(),
                # 身高
                'shengao': table('tr:nth-child(4) > td:nth-child(2) > strong').text(),
                # 惯用脚
                'guanyongjiao': table('tr:nth-child(4) > td:nth-child(4) > strong > span > strong').text(),
                # 国籍
                'guoji': table('tr:nth-child(5) > td:nth-child(2) > span > strong').text(),
                # 合同截止期
                'hetongjiezhiqi': table('tr:nth-child(5) > td:nth-child(4) > strong').text()
            }
            cursor.execute(sql_insert, insert_data)
            conn.commit()
            print(player, '：写入完成')
        except:
            print('写入异常')
            continue


def main():
    team_id_list = get_teams_list(team_list_url)
    print(team_id_list)
    player_id_list = get_player_list(team_id_list, player_list_url)
    print(player_id_list)
    get_player_info(player_id_list, player_info_url)


if __name__ == '__main__':
    main()
