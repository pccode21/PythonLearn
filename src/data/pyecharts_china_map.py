# pip install -i https://pypi.douban.com/simple pyecharts==1.6.2
import json, requests, datetime
import jsonpath
from pyecharts.charts import Map
import pyecharts.options as opts
import os

os.chdir(r'.\PythonLearn\src\data\images')  # 创建工作路径
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def catch_cn_disease_dis():  # 获取全国确诊分布数据 https://news.qq.com/zt2020/page/feiyan.htm
    print(timestamp)
    url_area = ('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=') + timestamp
    print(url_area)
    world_data = json.loads(requests.get(url=url_area).json()['data'])
    print(world_data)
    china_data = jsonpath.jsonpath(world_data, expr='$.areaTree[0].children[*]')
    print(china_data)
    # $	根对象, areaTree[0]定位中国，children[*]定位中国下的所有区域
    ls_province_names = jsonpath.jsonpath(china_data, expr='$[*].name')  # 定位区域名称
    print(ls_province_names)
    ls_confirm_vals = jsonpath.jsonpath(china_data, expr='$[*].total.confirm')  # 定位确认总数
    print(ls_confirm_vals)
    ls_province_confirm = list(zip(ls_province_names, ls_confirm_vals,))
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
    # 使用 list() 转换来输出列表
    return ls_province_confirm, world_data


# 绘制全国疫情地图
def map_cn_disease_dis() -> Map:
    # ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型，从而方便开发人员使用。
    map = (
        Map()
        .add('中国', ls_province_cfm, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情地图（确诊数）',
            subtitle='数能工作室制作\r\n最新更新时间%s\r\n数据来源腾讯' % format(timestamp)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                split_number=6,
                is_piecewise=True,  # 是否为分段型
                pos_top='center',
                pieces=[
                    {'min': 10000, 'color': '#7f1818'},  # 不指定 max
                    {'min': 1000, 'max': 10000},
                    {'min': 500, 'max': 999},
                    {'min': 100, 'max': 499},
                    {'min': 10, 'max': 99},
                    {'min': 0, 'max': 5}]
            )
        )
    )
    return map


def catch_gd_disease_dis():  # 获取广东省确诊分布数据
    dic_world_data = catch_cn_disease_dis()[1]  # 获取 world_data
    dic_gd_cfm = dict()  # dict() 函数用于创建一个字典。
    dic_gd = jsonpath.jsonpath(dic_world_data, expr='$.areaTree[0].children[?(@.name=="广东")].children[*]')
    # $ 根对象,areaTree[0]定位中国
    # [?(<expression>)] 过滤表达式。表达式必须计算为布尔值。
    # @ 过滤谓词正在处理的当前节点。
    # .<name> 点号的孩子(child)
    # * 通配符。可在任何需要名称或数字的地方使用。
    for item in dic_gd:
        if item['name'] not in dic_gd_cfm:
            if item['name'] == '地区待确认':  # 将‘地区待确认’更改为‘云浮’
                item['name'] = '云浮'
            dic_gd_cfm.update({item['name']: 0})  # 字典列表的取值从0开始计算
            # update() 函数把字典{item['name']: 0}的键/值对更新到dic_gd_cfm里。
        dic_gd_cfm[item['name']] += int(item['total']['confirm'])
    print(list(dic_gd_cfm.keys()))
    return dic_gd_cfm


# 绘制广东省疫情地图
def map_gd_disease_dis() -> Map:
    # ->常常出现在python函数定义的函数名后面，为函数添加元数据,描述函数的返回类型，从而方便开发人员使用。
    ls_gd_cities = [name + '市' for name in dic_gd_cfm.keys()]
    # Python3使用dict.keys()返回的是迭代器(如同遍历一般)
    map = (
        Map(init_opts=opts.InitOpts(width="900px", height="700px"))
        .add('广东省', [list(z) for z in zip(ls_gd_cities, dic_gd_cfm.values())], '广东', is_map_symbol_show=False)
        # Python3的keys(), values(), items()返回的都是迭代器，如果需要像Python2一样返回列表，只要传给list就行了
        # is_map_symbol_show=False 表示不显示符号
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter='{b}\n{c}例'))  # 设置图例
        # 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
        .set_global_opts(
            title_opts=opts.TitleOpts(title='广东省新型冠状病毒疫情地图（确诊数）',
            subtitle='数能工作室制作\r\n最新更新时间%s\r\n数据来源腾讯' % format(timestamp)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                split_number=6,
                is_piecewise=True,   # 是否为分段型
                pos_top='center',
                pieces=[
                    {'min': 50},
                    {'min': 30, 'max': 49},
                    {'min': 20, 'max': 29},
                    {'min': 10, 'max': 19},
                    {'min': 1, 'max': 9},
                    {'value': 0, "label": '无确诊病例', "color": 'green'}
                ]
            )
        )
    )
    return map


if __name__ == '__main__':
    ls_province_cfm, dic_world_data = catch_cn_disease_dis()
    print(ls_province_cfm)
    map_cn_disease_dis().render('全国疫情地图.html')
    dic_gd_cfm = catch_gd_disease_dis()
    print(dic_gd_cfm)
    map_gd_disease_dis().render('广东省疫情地图.html')
