import numpy as np  # numpy - Python的数值计算扩展工具包
import pandas as pd  # pandas - 基于Numpy的数据处理工具包
import matplotlib.pyplot as plt  # matplotlib - Python的绘图工具包
import seaborn as sns  # seaborn - matplotlib基础上的高级可视化工具包
import os
from matplotlib.font_manager import FontProperties


sns.set_style('darkgrid', {'font.sans-serif': ['simhei', 'Arial']})
# 解决Seaborn中文显示问题
# 设置图表风格
# Seaborn中有五种可供选择的主题：darkgrid(灰色网格)/whitegrid(白色网格)/dark(黑色)/white(白色)/ticks(十字叉)
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置-黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
os.chdir(r'.\PythonLearn\src\data')  # 创建工作路径
df = pd.read_excel('中国奥运运动员数据.xlsx', sheet_name='中国队', header=0)
df_length = len(df)
df_columns = df.columns.tolist()
data = df[['name', 'event', 'gender', 'height']]  # 数据筛选
# data.dropna(inplace=True)  # 去掉缺失值
# 提取男女数据
data_male = data[data['gender'] == '男']
data_female = data[data['gender'] == '女']
# 计算男女平均身高
hmean_male = data_male['height'].mean()
hmean_female = data_female['height'].mean()
plt.figure(figsize=(10, 5))  # 设置画布大小
# 绘制男女高度分布密度图
"""
seaborn.distplot(a, bins=None, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None, rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None, label=None, ax=None)
参数：a：Series、1维数组或者列表。

观察数据。如果是具有name属性的Series对象，则该名称将用于标记数据轴。

bins：matplotlib hist()的参数，或None。可选参数。

直方图bins（柱）的数目，若填None，则默认使用Freedman-Diaconis规则指定柱的数目。

hist：布尔值，可选参数。

是否绘制（标准化）直方图。

kde：布尔值，可选参数。

是否绘制高斯核密度估计图。

rug：布尔值，可选参数。

是否在横轴上绘制观测值竖线。

fit：随机变量对象，可选参数。

一个带有fit方法的对象，返回一个元组，该元组可以传递给pdf方法一个位置参数，该位置参数遵循一个值的网格用于评估pdf。

{hist, kde, rug, fit}_kws：字典，可选参数。

底层绘图函数的关键字参数。

color：matplotlib color，可选参数。

可以绘制除了拟合曲线之外所有内容的颜色。

vertical：布尔值，可选参数。

如果为True，则观测值在y轴显示。

norm_hist：布尔值，可选参数。

如果为True，则直方图的高度显示密度而不是计数。如果绘制KDE图或拟合密度，则默认为True。

axlabel：字符串，False或者None，可选参数。

横轴的名称。如果为None，将尝试从a.name获取它；如果为False，则不设置标签。

label：字符串，可选参数。

图形相关组成部分的图例标签。

ax：matplotlib axis，可选参数。

若提供该参数，则在参数设定的轴上绘图。

返回值：ax：matplotlib Axes

返回Axes对象以及用于进一步调整的绘图。

另请参见

kdeplot

显示具有核密度估计图的单变量或双变量分布。

rugplot

绘制小的垂直线以显示分布中的每个观测值。
"""
sns.distplot(data_male['height'], hist=False, kde=True, rug=True,  # 男生的身高
            rug_kws={'color': 'y', 'lw': 2, 'alpha': 0.5, 'height': 0.15},  # 设置数据频率分布颜色
            kde_kws={"color": "y", "lw": 1.5, 'linestyle': '--'},  # 设置密度曲线颜色，线宽，标注、线形
            label='男子身高')  # 设置图例
sns.distplot(data_female['height'], hist=False, kde=True, rug=True,  # 女生的身高
            rug_kws={'color': 'g', 'lw': 2, 'alpha': 0.5, 'height': 0.1},  # 设置数据频率分布颜色
            kde_kws={"color": "g", "lw": 1.5, 'linestyle': '--'},  # 设置密度曲线颜色，线宽，标注、线形
            label='女子身高')  # 设置图例
# 绘制运动员平均身高辅助线
plt.axvline(hmean_male, color='y', linestyle=":", alpha=0.8)
plt.text(hmean_male+1, 0.01, '男子平均身高: %.1f cm' % (hmean_male), color='y')  # ‘hmean_male+1, 0.01’是X轴和y轴坐标
plt.axvline(hmean_female, color='g', linestyle=":", alpha=0.8)
plt.text(hmean_female+1, 0.015, '女子平均身高: %.1f cm' % (hmean_female), color='g')  # ‘hmean_female+1, 0.015’是X轴和y轴坐标
# 调整图表细节，输出并保存
plt.xlim([120, 240])  # x轴边界
plt.ylim([0, 0.05])   # 调整Y轴刻度
plt.xlabel('身高', fontsize=10)  # 设置x轴标签说明
plt.title('中国运动员身高', fontsize=12)    # 添加图表名 China athlete's height
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./images/LOGO.ico')
thismanager.canvas.set_window_title('林旭东的可视化图表')
plt.savefig(r'./images/pic-1.png', dpi=400)  # 保存图表
plt.show()
