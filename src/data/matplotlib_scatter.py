import matplotlib.pyplot as plt
import matplotlib
import numpy as np
font = {'family': 'Microsoft Yahei', 'size': '8'}  # 设置才可以正常现在中文
matplotlib.rc('font', **font)
# x = [1, 3, 5, 7, 9]
# y = [2, 4, 6, 8, 10]
# x = list(range(1, 50))
# y = [x**2 for x in x]  # y的值是x的平方
n = 50  # 50个随机数
x = np.random.normal(0, 1, n)  # 平均值为0，方差为1
y = np.random.normal(0, 1, n)
# 散点
plt.scatter(x, y, linewidth=2, color='blue', label='scatter', alpha=0.5, marker='*')  # scatter是散点图
plt.legend()  # 添加图例
# 设置标题
plt.title("散点图", fontsize=12)
# 设置x轴
plt.xlabel("x", fontsize=12)
# 设置y轴
plt.ylabel("y", fontsize=12)
plt.Figure(figsize=(10, 10), dpi=80)
# 创建自定义图像
# figsize显示图像显示的位置
# 在图像模糊的时候，可以传入dpi参数，让图片更加清晰
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./PythonLearn/src/spider/win007/LOGO.ico')
thismanager.canvas.set_window_title('足球心经的可视化图表')
# plt.grid(True)  # 设置网格线
plt.savefig(r'./PythonLearn/src/data/images/scatter1.png')  # 保存图片
# 显示
plt.show()
