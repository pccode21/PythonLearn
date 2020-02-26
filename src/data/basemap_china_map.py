"""
https://www.lfd.uci.edu/~gohlke/pythonlibs/
pip install pyproj-2.5.0-cp38-cp38-win_amd64.whl  (地图投影和坐标转换库)
pip install basemap-1.2.1-cp38-cp38-win_amd64.whl
"""
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
m = Basemap(width=12000000,height=9000000,projection='cass',
            resolution='h',llcrnrlon=80.33,
              llcrnrlat=3.01,
              urcrnrlon=138.16,
              urcrnrlat=56.123,
              lat_0 = 42.5,lon_0=120)
m.drawcoastlines()  # 绘制海岸线
m.drawcountries()  # 划定国家边界
m.drawcounties()  # 划定洲界
m.etopo()  # 在地图上绘制etopo浮雕图像
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap(r'./PythonLearn/src/spider/win007/LOGO.ico')
thismanager.canvas.set_window_title('数能工作室制作')
plt.savefig(r'./PythonLearn/src/data/images/china_map.png')  # 保存图片
plt.show()
"""
参数介绍如下：
width：宽度。
height：高度。
projection='lcc'：表示规定的投影方法，改变投影方法绘制的结果也将不同，25种方式。
resolution=None：表示跳过处理边界数据集。
lat_0=50： 维度设置为50（Latitude，值为-90到90）。
lon_0=-107：经度设置为-107（Longitude，值为-180到180）
projection=merc'：表示规定的投影方法，墨卡托投影（Mercator Projection），广泛应用谷歌地图。
llcrnrlat=-80：所需地图域左下角的纬度（度）Latitude。
urcrnrlat=80：所需地图域的右上角的纬度（度）Latitude。
llcrnrlon=-180：所需地图域左下角的经度（度）Longitude。
urcrnrlon=180：所需地图域（度）的右上角的经度Longitude
"""
"""
用Basemap画出亚洲主要城市和人口
https://www.cnblogs.com/vamei/archive/2012/09/16/2687954.html
"""
