import numpy as np
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line, Page
from pyecharts.commons.utils import JsCode
import os
from pyecharts.render import make_snapshot  # 导入输出图片工具
from snapshot_selenium import snapshot  # 使用snapshot-selenium 渲染图片


os.chdir(r'./PythonLearn/src/spider/china_population')  # 创建工作路径
# 人口数量excel文件保存路径
POPULATION_EXCEL_PATH = 'population.xlsx'
# 读取标准数据
DF_STANDARD = pd.read_excel(POPULATION_EXCEL_PATH)
# 自定义pyecharts图形背景颜色js
background_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
)
# 自定义pyecharts图像区域颜色js
area_color_js = (
    "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
    "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
)


def analysis_total():  # 分析总人口
    x_data = DF_STANDARD['年份']  # 处理数据
    y_data = DF_STANDARD['年末总人口(万人)'].map(lambda x: '%.2f' % (x/10000))  # 将人口单位转换为亿
    # 自定义曲线图
    line = (
        Line(init_opts=opts.InitOpts(bg_color=JsCode(background_color_js)))  # 初始化配置项，参考 `global_options.InitOpts`
            .add_xaxis(xaxis_data=['{:0>4d}'.format(s) for s in range(1949, 2020)])
            # .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="总人口",
            y_axis=y_data,  # 系列数据
            is_smooth=True,  # 是否平滑曲线
            is_symbol_show=True,  # 是否显示 symbol标记
            symbol="pin",
            # 标记为圆针型，
            # symbol='path://M100,200 C100,100 250,100 250,200 S400,300 400,200',
            # svg图引入,svg图用notepad++软件或者记事本打开，将d属性值复制出来前面加path://即可
            # ECharts 提供的标记类型包括 'circle'圆, 'rect'正方, 'roundRect'圆正方, 'triangle'三角,'diamond'菱形, 'pin'圆针, 'arrow'箭头, 'none'
            # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI
            symbol_size=5,
            # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高
            # 例如 [20, 10] 表示标记宽为 20，高为 10
            linestyle_opts=opts.LineStyleOpts(color="#fff"),  # 线样式配置项，参考 `series_options.LineStyleOpts`
            label_opts=opts.LabelOpts(is_show=False, position="top", color="white"),  # 标签配置项，参考 `series_options.LabelOpts`
            itemstyle_opts=opts.ItemStyleOpts(  # 图元样式配置项，参考 `series_options.ItemStyleOpts`
                color="red", border_color="#fff", border_width=1
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),  # 提示框组件配置项，参考 `series_options.TooltipOpts`
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),  # 填充区域配置项，参考 `series_options.AreaStyleOpts`
            # 标出4个关键点的数据
            markpoint_opts=opts.MarkPointOpts(  # 标记点配置项，参考 `series_options.MarkPointOpts`
                data=[opts.MarkPointItem(name="新中国成立（1949年）", coord=[0, y_data[0]], value=y_data[0]),
                      opts.MarkPointItem(name="计划生育（1980年）", coord=[31, y_data[31]], value=y_data[31]),
                      opts.MarkPointItem(name="放开二胎（2016年）", coord=[67, y_data[67]], value=y_data[67]),
                      opts.MarkPointItem(name="2019年", coord=[70, y_data[70]], value=y_data[70])
                      ]
            ),
            # markline_opts 可以画直线
            # markline_opts=opts.MarkLineOpts(
            #     data=[[opts.MarkLineItem(coord=[39, y_data[39]]),
            #            opts.MarkLineItem(coord=[19, y_data[19]])],
            #           [opts.MarkLineItem(coord=[70, y_data[70]]),
            #            opts.MarkLineItem(coord=[39, y_data[39]])]],
            #     linestyle_opts=opts.LineStyleOpts(color="red")
            # ),
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="新中国70年人口变化(亿人)",
                pos_bottom="10%",  # title离底部的位置
                pos_left="center",  # 设置title居中
                title_textstyle_opts=opts.TextStyleOpts(color="#fff", font_size=16),
            ),
            # x轴相关的选项设置
            xaxis_opts=opts.AxisOpts(
                type_="category",  # 'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#ffffff63"),  # rotate=-40设置x轴标标签旋转角度
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,  # x坐标轴刻度的长度
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            # y轴相关选项设置
            yaxis_opts=opts.AxisOpts(
                name='人口（亿）',  # 设置y轴名称
                type_="value",  # 'value' 数值轴，适用于连续数据。
                # max_=16,  # 设置y轴最大取值范围
                position="left",
                interval=1,  # 设置y轴刻度间隔为1
                axislabel_opts=opts.LabelOpts(margin=20, color="#ffffff63"),
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=0, color="#ffffff1f")
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=False,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff1f"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False, linestyle_opts=opts.LineStyleOpts(color="#ffffff1f")
                ),
            ),
            # 图例配置项相关设置
            legend_opts=opts.LegendOpts(is_show=False, pos_left="10%", pos_top="5%"),
        )
    )
    make_snapshot(snapshot, line.render(), 'line.png')  # 输出保存为图片
    # page = Page(layout=Page.DraggablePageLayout)  # DraggablePageLayout表示可拖拽
    # page.add(line)
    # page.render('population_total.html')  # 渲染图像，将图像显示在一个html中


if __name__ == '__main__':
    analysis_total()
