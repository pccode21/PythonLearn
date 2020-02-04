import numpy as np  # numpy - Python的数值计算扩展工具包
import pandas as pd  # pandas - 基于Numpy的数据处理工具包
import matplotlib.pyplot as plt  # matplotlib - Python的绘图工具包
import seaborn as sns  # seaborn - matplotlib基础上的高级可视化工具包
import os


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
sns.set_style('darkgrid')  # 设置图表风格
# Seaborn中有五种可供选择的主题：darkgrid(灰色网格)/whitegrid(白色网格)/dark(黑色)/white(白色)/ticks(十字叉)
# 绘制男女高度分布密度图
sns.distplot(data_male['height'], hist=False, kde=True, rug=True,  # 男生的身高
            rug_kws={'color': 'y', 'lw': 2, 'alpha': 0.5, 'height': 0.1},  # 设置数据频率分布颜色
            kde_kws={"color": "y", "lw": 1.5, 'linestyle': '--'},  # 设置密度曲线颜色，线宽，标注、线形
            label='male_height')  # 设置图例
sns.distplot(data_female['height'], hist=False, kde=True, rug=True,  # 女生的身高
            rug_kws={'color': 'g', 'lw': 2, 'alpha': 0.5, 'height': 0.15},  # 设置数据频率分布颜色
            kde_kws={"color": "g", "lw": 1.5, 'linestyle': '--'},  # 设置密度曲线颜色，线宽，标注、线形
            label='female_height')  # 设置图例
# 绘制运动员平均身高辅助线
plt.axvline(hmean_male, color='y', linestyle=":", alpha=0.8)
plt.text(hmean_male+1, 0.01, 'male_height_mean: %.1f cm' % (hmean_male), color='y')
plt.axvline(hmean_female, color='g', linestyle=":", alpha=0.8)
plt.text(hmean_female+1, 0.015, 'female_height_mean: %.1f cm' % (hmean_female), color='g')
# 调整图表细节，输出并保存
plt.xlim([120, 240])  # x轴边界
plt.ylim([0, 0.05])               # 调整Y轴刻度
plt.title("China athlete's height", fontsize=11)    # 添加图表名
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./images/LOGO.ico')
thismanager.canvas.set_window_title('林旭东的可视化图表')
plt.savefig(r'./images/pic-1.png', dpi=400)  # 保存图表
plt.show()
