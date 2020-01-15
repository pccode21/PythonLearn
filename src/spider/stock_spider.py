import re
import requests
import json
from pyquery import PyQuery
import pymysql


stock_list_url = 'https://hq.gucheng.com/gpdmylb.html'
stock_info_url = 'http://qd.10jqka.com.cn/quote.php?cate=real&type=stock&return=json&callback=showStockData&code='
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def connect():
    conn = pymysql.connect(host='localhost',
                            port=3306,
                            user='root',
                            password='Lxd05230708',
                            database='spider',
                            charset='utf8mb4')
    cursor = conn.cursor()
    return{'conn': conn, 'cursor': cursor}


connection = connect()
conn, cursor = connection['conn'], connection['cursor']
sql_insert = "insert into stock(code, name, jinkai, chengjiaoliang, zhenfu, zuigao, chengjiaoe, huanshou, zuidi, zuoshou, liutongshizhi, create_time) values (%(code)s, %(name)s, %(jinkai)s, %(chengjiaoliang)s, %(zhenfu)s, %(zuigao)s, %(chengjiaoe)s, %(huanshou)s, %(zuidi)s, %(zuoshou)s, %(liutongshizhi)s, now())"


def get_stock_list(stockListURL):
    r = requests.get(stockListURL, headers=headers)
    doc = PyQuery(r.text)
    list = []
    # 获取所有 section 中 a 节点，并进行迭代
    for i in doc('.stockTable a').items():
        try:
            href = i.attr.href
            list.append(re.findall(r'\d{6}', href)[0])
            # r'\d{6}'表示提取href中的6个数字
            # re.findall提取出的信息是列表存储的，[0]即是将列表中的第一个数据从列表中提出来
        except:
            continue
    # list = [item.lower() for item in list]  # 将爬取信息转换小写
    return list


def get_stock_info(list, stockInfoURL):
    for stock in list:
        try:
            url = stockInfoURL + stock
            r = requests.get(url, headers=headers)
            # r返回的结果是：showStockDate({"info":{"000001":{"name":"\u5e73\u5b89\u94f6\u884c"}},"data":{"000001":{"10":"16.13","8":"16.14","9":"15.87","13":"78795234.00","19":"1262802470.00","7":"16.12","15":"40225508.00","14":"37528826.00","69":"17.73","70":"14.51","12":"5","17":"945400.00","264648":"0.010","199112":"0.062","1968584":"0.406","2034120":"9.939","1378761":"16.026","526792":"1.675","395720":"-948073.000","461256":"-39.763","3475914":"313014790000.000","1771976":"1.100","6":"16.12","11":""}}})
            # 将获取到的数据封装进字典
            dict1 = json.loads(r.text[14: int(len(r.text)) - 1])
            # “r.text[14: int(len(r.text)) - 1]”是去掉 JSONP 返回的标准格式的数据的头“showStockDate(”和尾“）”
            # 这样处理的结果才是标准的JSON数据
            print(dict1)
            # 获取字典中的数据构建写入数据模版
            insert_data = {
                'code': stock,
                'name': dict1['info'][stock]['name'],
                'jinkai': dict1['data'][stock]['7'],
                'chengjiaoliang': dict1['data'][stock]['13'],
                'zhenfu': dict1['data'][stock]['526792'],
                'zuigao': dict1['data'][stock]['8'],
                'chengjiaoe': dict1['data'][stock]['19'],
                'huanshou': dict1['data'][stock]['1968584'],
                'zuidi': dict1['data'][stock]['9'],
                'zuoshou': dict1['data'][stock]['6'],
                'liutongshizhi': dict1['data'][stock]['3475914']
            }
            cursor.execute(sql_insert, insert_data)
            conn.commit()
            print(stock, '：写入完成')
        except:
            print('写入异常')
            # 遇到错误继续循环
            continue


def main():
    list = get_stock_list(stock_list_url)
    print(list)
    get_stock_info(list, stock_info_url)


if __name__ == '__main__':
    main()
