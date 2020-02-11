# pip install pyecharts==0.1.9.4
import json
from pyecharts import Map
import os
import codecs
from collections import Counter
# collections --- 容器数据类型
# Counter 字典的子类，提供了可哈希对象的计数功能,它是一个集合，元素像字典键(key)一样存储，它们的计数存储为值。

os.chdir(r'.\PythonLearn\src\spider\weixin')  # 指定工作路径


def counter2list(_counter):  # _counter=Property_counter
    name_list = []
    num_list = []
    for item in _counter:
        name_list.append(item[0])
        num_list.append(item[1])
    return name_list, num_list


def get_map(item_name, item_name_list, item_num_list):
    subtitle = '林旭东的可视化报表'
    _map = Map(item_name, width=1300, height=800, title_pos='center', title_text_size=30, subtitle=subtitle, subtitle_text_size=25)
    _map.add('', item_name_list, item_num_list, maptype='china', is_visualmap=True, visual_text_color='#000')
    out_file_name = 'data/' + item_name + '.html'
    _map.render(out_file_name)


if __name__ == '__main__':
    in_file_name = 'data/myfriends.json'
    with codecs.open(in_file_name, encoding='utf-8') as f:
        friends = json.load(f)
    Province_counter = Counter()  # 省份计算
    for friend in friends:
        if friend['Province'] != '':
            Province_counter[friend['Province']] += 1  # 统计省份数量
        print(Province_counter)
    name_list, num_list = counter2list(Province_counter.most_common(30))  # 省份前15
    print(name_list, num_list)
    get_map('微信好友地图可视化', name_list, num_list)
