# pip install -i https://pypi.douban.com/simple pyecharts==1.6.2
import json, requests, datetime, time
import jsonpath
from pyecharts.charts import Map
import pyecharts.options as opts
import os

os.chdir(r'.\PythonLearn\src\data\images')  # 创建工作路径
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def catch_cn_disease_dis():
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
    ls_confirm_vals = jsonpath.jsonpath(china_data, expr='$[*].total.confirm') # 定位确认总数
    print(ls_confirm_vals)
    ls_province_confirm = list(zip(ls_province_names, ls_confirm_vals,))
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
    # 使用 list() 转换来输出列表
    print(ls_province_confirm)
    return ls_province_confirm, world_data


ls_province_cfm, dic_world_data = catch_cn_disease_dis()
print(ls_province_cfm)


def map_cn_disease_dis() -> Map:
    map = (
        Map()
        .add('中国', ls_province_cfm, 'china')
        .set_global_opts(
            title_opts=opts.TitleOpts(title='全国新型冠状病毒疫情地图（确诊数）', subtitle='林旭东的可视化图表\r\n最新更新时间%s\r\n数据来源腾讯'%format(timestamp)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                split_number=6,
                is_piecewise=True,  # 是否为分段型
                pos_top='center',
                pieces=[
                                                   {'min': 10000, 'color': '#7f1818'},  #不指定 max
                                                   {'min': 1000, 'max': 10000},
                                                   {'min': 500, 'max': 999},
                                                   {'min': 100, 'max': 499},
                                                   {'min': 10, 'max': 99},
                                                   {'min': 0, 'max': 5}]
            )
        )
    )
    return map


map_cn_disease_dis().render('全国疫情地图.html')
