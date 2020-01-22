import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import font_manager


# 设置图表样式
plt.style.use('fivethirtyeight')
# 这里使用pandas读取csv文件
data = pd.read_csv(r'./PythonLearn/src/spider/win007/football_player.csv', encoding='utf-8')
print(data)
# 设置rc参数显示中文标题
plt.rcParams['font.family'] = ['sans-serif']  # 设置字体样式
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体为SimHei显示中文
countrys = data['nationality']
# 定义一个Counter
# 用来统计国家分类的总数
country_counter = Counter()
for country in countrys:
    country_counter.update(country.split(' '))
countries = []
popularity = []
# 取前15个
for item in country_counter.most_common(15):
    countries.append(item[0])
    popularity.append(item[1])
# 倒序显示
countries.reverse()
popularity.reverse()
# 设置图表的字体微软雅黑 防止中文乱码的
zh_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\simhei.ttf')
# 使用横向条形图表
plt.yticks(fontsize=8)  # 设置y轴字体大小
plt.barh(countries, popularity)  # barh()表示绘制水平方向的条形图
plt.title('英超球员国籍比例', fontproperties=zh_font)
plt.xlabel('人数', fontproperties=zh_font)
plt.tight_layout()
plt.Figure()  # 创建自定义图像
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./PythonLearn/src/spider/win007/LOGO.ico')
thismanager.canvas.set_window_title('足球心经的可视化图表')
plt.show()
