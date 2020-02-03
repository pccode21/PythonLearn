from matplotlib import pyplot as plt
import random
from matplotlib import font_manager
import matplotlib
import numpy as np


font = {'family': 'Microsoft Yahei', 'size': '8'}  # 设置才可以正常现在中文
matplotlib.rc('font', **font)
# 注释掉的是另一种方法字体设置
# 路径是需要自己电脑里面的
# my_font = font_manager.FontProperties(fname='C:\\Windows\\Fonts\\PingFang.ttc')
# x = range(2, 26, 2)
# y = [15, 13, 14, 5, 17, 20, 25, 26, 24, 22, 18, 15]
# plt.plot(x, y)
# plt.xticks(x)  # 设置x的刻度
# plt.xticks(x[::2])
# 当刻度太密集的时候使用列表的步长（间隔取值）来解决，matplotlib会帮助我们对应
# plt.xticks(range(1, 25))
# plt.xlim(1, 25)  # 设置x范围
# plt.ylim(1, 120) # 设置y范围
# x_ticks = np.arange(1, 13, 1)  # 设置x刻度
# plt.xticks(x_ticks)
# _xticks_labels = [i/2 for i in range(4, 49)]  # 设置x间隔为0.5
# plt.xticks(_xticks_labels[::3])  # 取步长每隔3取一个，也就是x间隔为1.5
# plt.yticks(range(min(y), max(y)+1))
x = range(120)
a = [random.randint(20, 35) for i in range(120)]
y = a
random.seed(10)
plt.rcParams['figure.figsize'] = (7.0, 6.5)  # 图片像素
# plt.subplot(1, 2, 1)  #建立一个高为1，宽为2的subplot网格，激活第一个网格
plt.plot(x, y, linewidth=1, color='green', label='random', linestyle='--')
# plot是曲线图，linewidth指定线条粗细
# 添加虚线样式：linestyle，linestyle取值：':'、'--'、'-.'、'-'
plt.title('曲线图', fontsize=9)  # 设置标题
plt.xlabel('时间', fontsize=9)  # 设置x轴标签说明
plt.ylabel('随机数值', fontsize=9)  # 设置y轴标签说明
plt.legend()  # 添加图例
_x_ticks = ['10点{}分'.format(i) for i in x if i<60]
_x_ticks += ['11点{}分'.format(i-60) for i in x if i>=60]
plt.xticks(x[::5], _x_ticks[::5], rotation=45)  # rotation设置x轴标签的字体倾斜角度
plt.Figure(figsize=(10, 10), dpi=80)
# 创建自定义图像
# figsize显示图像显示的位置
# 在图像模糊的时候，可以传入dpi参数，让图片更加清晰
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./PythonLearn/src/spider/win007/LOGO.ico')
thismanager.canvas.set_window_title('林旭东的可视化图表')
plt.savefig(r'./PythonLearn/src/data/images/sig_size.png')  # 保存图片
plt.show()
