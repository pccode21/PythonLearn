import requests
import time
import re


url_time = time.strftime('%Y%m%d%H%M%S')
team_list_url = 'http://zq.win007.com/jsData/matchResult/2019-2020/s36.js?version='+url_time
player_list_url = 'http://zq.win007.com/jsData/teamInfo/teamDetail/'
headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': 'zq.win007.com',
            'Referer': 'http://zq.win007.com/cn/League/2019-2020/36.html',  # 需要加入跳转网页
            'Connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'Cookie': 'win007BfCookie=0^0^1^1^1^1^1^0^0^0^0^0^1^2^1^1^0^1^1^0; UM_distinctid=16f82dd359f17e-0864fb7189f26a-c383f64-100200-16f82dd35a1123; CNZZDATA1261430177=958542710-1578443893-http%253A%252F%252Fzq.win007.com%252F%7C1579243197; bfWin007FirstMatchTime=2020,0,19,08,10,00'
            }


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


time.sleep(1)


def get_player_list(list, playerListURL):
    for i in list:
        time.sleep(1)
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
        time.sleep(1)
        for i in res:
            try:
                player_id = i[0]
                player_id_list.append(player_id)
            except:
                continue
        return player_id_list


def main():
    team_id_list = get_teams_list(team_list_url)
    print(team_id_list)
    player_id_list = get_player_list(team_id_list, player_list_url)
    print(player_id_list)


if __name__ == '__main__':
    main()
