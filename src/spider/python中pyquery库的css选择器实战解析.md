python中pyquery库的css选择器实战解析
======================================
1.pyquery部分选择器解释
----------------------------
```Python
"""pyquery的CSS选择器方法"""
from pyquery import PyQuery


html = """
<div id="container">
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tr class="h">
        <td class="l" width="374">职位名称</td>
        <td>职位类别</td>
        <td>人数</td>
        <td>地点</td>
        <td>发布时间</td>
    </tr>
</table>    
</div>
"""
# 传递html内容初始化
res = PyQuery(html)
# CSS选择器方法进行选择。#container为ID选择方法，.tablelist为class选择方法，tr为标签选择方法
# 这句的意思是选择ID为container节点内部的class为tablelist的节点中所有tr标签内容
print(res("#container .tablelist tr"))
# <class 'pyquery.pyquery.PyQuery'> 类型为PyQuery类型
print(type(res("#container .tablelist tr")))

"""
# 常用CSS选择器方法介绍
find()      查找结点的所有子孙节点
children()  查找子节点，也可以在括号中添加想要查找的子节点类型
parent()    获取目标的父节点
parents()   获取所有的祖先节点，可以在括号中添加css选择器选取想要的祖先节点
siblings()  兄弟节点，选择除本身之外的兄弟节点，可添加css选择器
# 选择完成之后会有许多节点，这需要遍历
items()     返回一个生成器,使用for循环就可以打印出来。循环的每一个节点还是PyQuery类型可以继续CSS选择器选择
# 获取属性和文本信息
attr()      获取找到的第一个属性，找多个需要循环遍历
text()      获取所有文本以空格分割开并合并成一个字符串
html()      获取找到的第一个html文本，找多个需要循环遍历
# 节点操作
addClass()      增加class属性
removeClass()   移除class属性
remove()        删除find("xx").remove()找到的指定内容
attr()          增加节点属性
text()          增加节点文本内容
html()          增加节点html内容
http://www.w3school.com.cn/css/index.asp    # CSS教程
"""


# 伪类选择器
doc = PyQuery(html)
# 第一个td节点
td = doc("td:first-child")
print(td)
# 最后一个td节点
td = doc("td:last-child")
print(td)
# 第二个td节点
td = doc("td:nth-child(2)")
print(td)
# 第三个td节点之后的td节点
td = doc("td:gt(2)")
print(td)
# 偶数位置的td节点
td = doc("td:nth-child(2n)")
print(td)
# 包含、地点、文本的td节点
td = doc("td:contains(地点)")
print(td)
```

2.pyquery三种解析方法的选择
----------------------------
```Python
"""CSS选择器库，熟悉web和jquery可以选择此解析库"""
from pyquery import PyQuery
import requests


# 第一种解析方法,直接传入url进行请求然后用得到的HTML内容进行初始化
res = PyQuery(url="https://www.sogou.com/")
# css中的标签选择方法打印title标签和内容
print(res("title"))


# 第二种常规解析方法,用网页的源代码以字符串的形式传递给PyQuery类来初始化
rew = PyQuery(requests.get("https://www.sogou.com/").text)
print(rew("title"))


# 文件解析.可以选取一个本地HTML文件进行解析
req = PyQuery(filename="index.html")
print(req("title"))
```
