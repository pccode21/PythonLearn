import numpy as np               # numpy - Python的数值计算扩展工具包
import pandas as pd              # pandas - 基于Numpy的数据处理工具包
import matplotlib.pyplot as plt  # matplotlib - Python的绘图工具包
import seaborn as sns            # seaborn - matplotlib基础上的高级可视化工具包
import os


sns.set_style('ticks', {'font.sans-serif': ['simhei', 'Arial']})
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
data = df[['name', 'event', 'height', 'weight']]  # 数据筛选
event_count = data['event'].value_counts()
event_select = event_count[event_count > 15]  # 赛选运动员数量多于15人的项目数据
print(event_select)
data2 = data[(data['event'] == '田径') |
            (data['event'] == '游泳') |
            (data['event'] == '篮球') |
            (data['event'] == '射击') |
            (data['event'] == '足球') |
            (data['event'] == '皮划艇') |
            (data['event'] == '赛艇') |
            (data['event'] == '曲棍球') |
            (data['event'] == '自行车')]
data2.dropna(how='all', inplace=True)  # 删除全空的行
data2['BMI'] = data2['height']/(data2['weight']/100)**2
# 计算运动员BMI指数；BMI计算公式：体重(kg)/(身高*身高(m))；由于源数据中身高的单位是cm,所以要对身高/100后再计算
plt.figure(figsize=(8, 4))  # 画布大小设置
colors = ["red", "orange", "green", "blue", "violet", "brown", "yellow", "black", "teal"]
sns.violinplot(x='event', y='BMI', data=data2,  # 绘制小提琴图,https://seaborn.pydata.org/generated/seaborn.violinplot.html
                scale='count',
                # 宽度以样本数量来显示，数据样本越多，小提琴图越宽
                # scale {“ area”，“ count”，“ width”}，可选用于缩放每个小提琴宽度的方法。
                # 如果是面积"area"，则每个小提琴将具有相同的面积。
                # 如果计数"count"，则小提琴的宽度将根据该仓中的观察次数进行缩放。
                # 如果宽"width"，则每个小提琴的宽度都相同。
                # palette='husl',
                # https://seaborn.pydata.org/tutorial/color_palettes.html
                # 设置调色盘颜色,seaborn提供了一个到husl系统的接口（自重命名为HSLuv），
                # 这也使得选择均匀分布的色相变得容易，同时又使外观亮度和饱和度更加均匀
                xkcd_palette='colors',  # 自定义配色盘颜色,从xkcd_rgb字典中提取单色,https://xkcd.com/color/rgb/
                inner='quartile')  # 内部显示为分位数
                # inner {“ box”，“ quatile”，“ point”，“ stick”，None}，
                # 可选表示小提琴内部的数据点。 如果是方框"box"，请绘制一个微型箱线图。
                # 如果是四分位数"quatile"，则绘制分布的四分位数。
                #如果是点"point"或棒"stick"，请显示每个基础数据点。
                # 使用“None”将绘制未经修饰的小提琴。
# 给小提琴图内部加上散点图，显示每项数据的具体分布情况
sns.swarmplot(x='event', y='BMI', data=data2, color="w", alpha=0.8, s=2)  # s是圆点的宽度
plt.xlabel('项目', fontsize=12)  # 设置x轴标签说明
plt.ylabel('BMI', fontsize=12)  # 设置y轴标签说明
plt.grid(linestyle='--')         # 添加网格线
plt.title("中国运动员的BMI指数", fontsize=14)  # 设置标题
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./images/LOGO.ico')
thismanager.canvas.set_window_title('林旭东的可视化图表')
plt.savefig(r'./images/pic-2.png', dpi=400)  # 保存图表
plt.show()
