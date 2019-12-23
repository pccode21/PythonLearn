import re
import os
import urllib.request
#根据给定的网址来获取网页详细信息，得到的html就是网页的源代码
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html.decode('UTF-8')
def getImg(html):
    reg = 'src="(.+?\.jpg)" pic_ext'  
    imgre = re.compile(reg) #转换成一个正则对象
    imglist = imgre.findall(html) #表示在整个网页中过滤出所有图片的地址，放在imglist中
    print("====图片的地址=====",imglist)
    x = 0 #声明一个变量赋值
    path = '/eclipse-workspace/pictures/' #设置保存地址，相对路径
    if not os.path.isdir(path):
        os.makedirs(path) # 将图片保存到文件夹，没有则创建
    print(path)
    print('图片已开始下载，注意查看文件夹') 
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'{0}{1}.jpg'.format(path,x)) #打开imglist，下载图片保存在本地，
        x = x + 1      
    return imglist
html = getHtml("http://tieba.baidu.com/p/3840085725") #获取该网址网页的源代码
print(getImg(html)) #从网页源代码中分析并下载保存图片