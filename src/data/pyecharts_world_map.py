import json, requests, datetime
import jsonpath
from pyecharts.charts import Map
import pyecharts.options as opts
import os

os.chdir(r'.\PythonLearn\src\data\images')  # 创建工作路径
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def catch_world_disease_dis():  # 获取全国确诊分布数据 https://news.qq.com/zt2020/page/feiyan.htm
    url_area = ('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=') + timestamp
    world_data = json.loads(requests.get(url=url_area).json()['data'])
    world_map_data = jsonpath.jsonpath(world_data, expr='$.areaTree[0:]')
    ls_country_names = jsonpath.jsonpath(world_map_data, expr='$[*].name')  # 定位国家名称
    ls_confirm_vals = jsonpath.jsonpath(world_map_data, expr='$[*].total.confirm')  # 定位确认总数
    ls_heal_vals = jsonpath.jsonpath(world_map_data, expr='$[*].total.heal')
    ls_country_confirm = list(zip(ls_country_names, ls_confirm_vals,))
    ls_country_heal = list(zip(ls_country_names, ls_heal_vals,))
    print('康复人数：', ls_country_heal)
    return ls_country_confirm, world_data, ls_country_heal


countries = ['China', 'Korea', 'Cruise', 'Italy', 'Iran', 'Japan', 'Singapore', 'Germany', 'United States',
        'Kuwait', 'Thailand', 'France', 'Bahrain', 'Malaysia', 'Australia',
        'United Arab Emirates', 'United Kingdom', 'Vietnam', 'Canada',
        'Spain', 'Sweden', 'Israel', 'Norway', 'Switzerland', 'Oman',
        'Iraq', 'Russia', 'Lebanon', 'India', 'Austria', 'Greece', 'Croatia',
        'Philippines', 'Denmark', 'Finland', 'Brazil', 'Algeria', 'Northern Macedonia',
        'Netherlands', 'Afghanistan', 'Nepal', 'Estonia', 'Cambodia', 'Georgia', 'Romania', 'Sri Lanka', 'Belgium']
country_name = catch_world_disease_dis()
names = []
vs = []
for n in range(len(country_name[0])):
    name = [country_name[0][n][0]]
    value = [country_name[0][n][1]]
    names.append(name)
    vs.append(value)
print(names)
print(vs)

data = []
for index in range(len(countries)):
    countries_values = [countries[index], vs[index]]
    data.append(countries_values)
# for index in range(len(country_name[0])):
    # countries = [country_name[0][index][0], country_name[0][index][1]]
    # data.append(countries)
print(data)


def map_world_disease_dis():
    subtitle_list = '数能工作室制作\r\n最新更新时间%s\r\n数据来源腾讯\r\n中国康复人数：%s人' % (format(timestamp),
    format(ls_countries_health[0][1]))
    map = (
        Map(init_opts=opts.InitOpts(width="900px", height="700px"))
        .add("世界疫情地图", data, "world", is_map_symbol_show=True, zoom=1.1)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title='中国加油！全人类加油！！',
            subtitle=subtitle_list,
            title_textstyle_opts=opts.TextStyleOpts(color='red',font_size=20),
            subtitle_textstyle_opts=opts.TextStyleOpts(color='black',font_size=15),item_gap=15),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                split_number=7,
                is_piecewise=True,item_width=24,item_height=12,textstyle_opts=opts.TextStyleOpts(font_size=12),  # 是否为分段型
                pos_top='center',
                pieces=[
                    {'min': 10000, 'color': '#7f1818'},  # 不指定 max
                    {'min': 1000, 'max': 10000},
                    {'min': 500, 'max': 999, 'label': '500 - 999 钻石号邮轮:%s人' % format(ls_country_cfm[1][1])},
                    {'min': 100, 'max': 499},
                    {'min': 10, 'max': 99},
                    {'min': 1, 'max': 5}]
            )
        )
    )
    return map


if __name__ == '__main__':
    ls_country_cfm, dic_world_data, ls_countries_health = catch_world_disease_dis()
    print(ls_country_cfm)
    print(dic_world_data)
    map_world_disease_dis().render('世界疫情地图.html')
    # map_world().render('世界地图.html')
