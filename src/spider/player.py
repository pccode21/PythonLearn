import requests
from pyquery import PyQuery
import pymysql

# 目标爬取链接
url = 'http://zq.win007.com/cn/team/player.aspx?PlayerID=99201&TeamID=25'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'referer': 'http://zq.win007.com/'
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


def get_data():
    """
    获取数据并将数据存入数据库
    :return:
    """
    response = requests.get(url, headers = headers)
    doc = PyQuery(response.text)
    # 获取整体数据 table
    table = doc('.tdlink')

    # 构造插入数据库数据
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

    print('数据写入完成')


def main():
    get_data()


if __name__ == '__main__':
    main()
