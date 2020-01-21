import csv
import os

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_state(player):  # 取球员详细数据的方法
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
    res = requests.get(player, headers=headers)   # get方法中加入请求头
    res.encoding = 'gbk'
    soup = BeautifulSoup(res.text, 'lxml')  # 对返回的结果进行解析
    state = list(soup.find(class_='txt').find_all('dd'))
    print(state)
    for x in range(len(state)):
        state[x] = str(state[x])[4:-5]
    return state


with open(r'./PythonLearn/src/spider/players/playerlinks.csv', 'r') as f:  # 打开球员链接文件
    reader = csv.reader(f)
    column1 = [row[1]for row in reader]
player = list()  # 新建存储球员数据的列表
for x in column1:
    player.append(get_state(x))

p_columns = ['中文名称', '英文名称', '英文全称', '生日', '身高', '体重', '年龄', '位置', '国籍', '俱乐部', '球衣号码']
raw_list = pd.DataFrame(columns=p_columns, data=player)  # 把嵌套列表转化为DataFrame对象
raw_list.to_csv(r'./PythonLearn/src/spider/players/player.csv', encoding='gbk')  # 存储为csv文件
