"""pyquery实战解析之数据存储"""
import requests
from pyquery import PyQuery


# 获取请求头信息
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
# 发送get请求并获取请求的文本字符串
for i in range(1, 11):
    url = "https://www.gushiwen.org/default_"+str(i)+".aspx"
    print('正在爬取的链接为：%s' % url)
    response = requests.get(url=url, headers=headers)
    print('正在获取第 %d 页' % i)
    # 将获取的文本字符串转换为PyQuery对象
    doc = PyQuery(response.text)
    # 循环遍历，使用css选择器并调用items()方法生成迭代器
    for item in doc(".cont").items():
        # 调用find()方法并采用css选择器中的标签选择获取标题。
        title = item.find("p b").text()
    # 获取结果类型为字符串，可以调用split()方法进行分割。分割之后为列表类型
        contents = item.find("p a").text().split(" ")
    # 根据获得的结果进行判断
        if len(contents) == 1:
            continue
    # 朝代
        dynasty = contents[1]
    # 作者
        author = contents[2]
    # 调用children()方法并采用css选择器中的标签选择获取文本内容
        text = item.children(".contson").text()
    # f = open("poetry.txt", "a", encoding="utf-8")
    # f.write("\n".join([title, dynasty, author, text]))
    # f.write("\n" + "=" * 100 + "\n")
    # f.close()     # 此种文件操作模式完成之后需要调用close()方法主动关闭文件
    # 打开.txt文件，以"a"追加的方式写入utf-8编码的数据内容并给出可操作的文件句柄f
        with open(r'./PythonLearn/src/spider/poetry.txt', 'a', encoding="utf-8") as f:
            # with as 语法执行文件操作之后会自动关闭打开的文件，所以不用调用close()方法
            f.write("\n".join([title, dynasty, author, text]))
            f.write("\n" + "=" * 20 + "\n")
