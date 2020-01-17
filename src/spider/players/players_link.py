# encoding:UTF-8
import csv
import requests
from bs4 import BeautifulSoup
with open(r'./PythonLearn/src/spider/players/teamlinks.csv', 'r') as f:  # 取球队链接
    reader = csv.reader(f)
    column1 = [row[1]for row in reader]
player = {}  # 建存储球员链接的字典
for x in column1:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    url = x
    res = requests.get(url, headers=headers)  # get方法中加入请求头
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text, 'lxml')  # 对返回的结果进行解析
    player_name = soup.find(class_='sub03_c').find_all('p')  # 找球员姓名
    # 因为class是python的关键字，所以在写过滤的时候,凡是写在[ ]里面的都是class，外面的是class_
    for i in range(len(player_name)):
        player_name[i] = str(player_name[i].get_text())
    player_links = soup.find(class_='sub03_c').find_all('a')  # 找球员链接
    for j in range(len(player_links)):
        player_links[j] = str(player_links[j].attrs['href'])  # 取href属性
    for k in range(len(player_name)):
        player[str(player_name[k])] = str(player_links[k])
        # 将球员姓名和球员链接连接起来，'球员姓名':'球员链接'
with open(r'./PythonLearn/src/spider/players/playerlinks.csv', 'w') as f:  # 写入球员链接
    [f.write('{0},{1}\n'.format(key, value)) for key, value in player.items()]
