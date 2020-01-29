# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.style.use('ggplot')  # matplotlib> = 1.4，有一个新的样式模块，默认情况下具有 ggplot 样式
# 定义字体
font = FontProperties(fname=r'c:\windows\fonts\simsun.ttc', size=9)
ax1 = plt.subplot(2, 2, 1, projection='polar')  # polar是极面图
ax2 = plt.subplot(2, 2, 2, projection='polar')
ax3 = plt.subplot(2, 2, 3, projection='polar')
ax4 = plt.subplot(2, 2, 4, projection='polar')

ability_size = 6  # 这是极面图的y轴
ability_label = [u'进攻', u'防守', u'盘带', u'速度', u'体力', u'射术']
player = {
    'M': np.random.randint(size=ability_size, low=60, high=99),
    'H': np.random.randint(size=ability_size, low=60, high=99),
    'P': np.random.randint(size=ability_size, low=60, high=99),
    'Q': np.random.randint(size=ability_size, low=60, high=99)
}

theta = np.linspace(0, 2*np.pi, 6, endpoint=False)  # 这是极面图的x轴
# np.pi 是一个常数表示圆周率π，2*np.pi就相当于2π
# np.linspace主要用来创建等差数列
# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# start:返回样本数据开始点，这里是0
# stop:返回样本数据结束点，这里是2*np.pi
# num:生成的样本数据量，这里是6
# endpoint：True则包含stop；False则不包含stop
theta = np.append(theta, theta[0])

player['M'] = np.append(player['M'], player['M'][0])
ax1.plot(theta, player['M'], 'r')
ax1.fill(theta, player['M'], 'r', alpha=0.3)
# 设置坐标刻度
ax1.set_xticks(theta)
ax1.set_xticklabels(ability_label, y=0.1, FontProperties=font)
ax1.set_title(u'梅西', FontProperties=font, color='r', size=20)

player['H'] = np.append(player['H'], player['H'][0])
ax2.plot(theta, player['H'], 'g')
ax2.fill(theta, player['H'], 'g', alpha=0.3)
# 设置坐标刻度
ax2.set_xticks(theta)
ax2.set_xticklabels(ability_label, y=0.1, FontProperties=font)
ax2.set_title(u'德容', FontProperties=font, color='g', size=20)

player['P'] = np.append(player['P'], player['P'][0])
ax3.plot(theta, player['P'], 'b')
ax3.fill(theta, player['P'], 'b', alpha=0.3)
# 设置坐标刻度
ax3.set_xticks(theta)
ax3.set_xticklabels(ability_label, y=0.1, FontProperties=font)
ax3.set_title(u'布斯克茨', FontProperties=font, color='b', size=20)

player['Q'] = np.append(player['Q'], player['Q'][0])
ax4.plot(theta, player['Q'], 'y')
ax4.fill(theta, player['Q'], 'y', alpha=0.3)
# 设置坐标刻度
ax4.set_xticks(theta)
ax4.set_xticklabels(ability_label, y=0.1, FontProperties=font)
ax4.set_title(u'卡塞米罗', FontProperties=font, color='y', size=20)
plt.tight_layout()  # 设置自动调整子图这间的间隔
plt.Figure(figsize=(10, 10), dpi=80)
# 创建自定义图像
# figsize显示图像显示的位置
# 在图像模糊的时候，可以传入dpi参数，让图片更加清晰
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./PythonLearn/src/spider/win007/LOGO.ico')
thismanager.canvas.set_window_title('足球心经的可视化图表')
plt.savefig(r'./PythonLearn/src/data/images/polar.png')  # 保存图片
plt.show()
