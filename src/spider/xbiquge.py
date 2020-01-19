import requests
import re
import pymysql


def get_data():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }
    # 小说目录URL
    url = 'http://www.xbiquge.la/0/215/'
    html = requests.get(url, headers=headers).content.decode('utf-8')
    pat = r"<dd><a href='(.*?)' >(.*?)</a></dd>"
    get_list = re.findall(pat, html)
    return get_list


def db_connect(get_list):
    for i in get_list:
        title_url = i[0]
        title_name = i[1]
        newUrl = 'http://www.xbiquge.la' + title_url
        # 连接数据库，参数包括IP、用户名、密码、对应的库名
        connect = pymysql.connect(host='localhost',
                                    port=3306,
                                    user='root',
                                    password='Lxd05230708',
                                    database='spider',
                                    charset='utf8mb4')
        # 数据库游标
        course = connect.cursor()
        # 插入语句
        sql = "INSERT INTO kongfu values(default, '%s', '%s')" % (title_name, newUrl)
        # 数据表中id要设置成 `id` INT NOT NULL AUTO_INCREMENT 和 PRIMARY KEY (`id`)
        try:
            print("正在写入数据 ---->>>>: ", title_name)
            course.execute(sql)
            connect.commit()
        except Exception as e:
            print('数据写入失败!', e)
            connect.rollback()
            connect.close()
    course.close()
    connect.close()


def main():
    get_list = get_data()
    db_connect(get_list)


if __name__ == '__main__':
    main()
