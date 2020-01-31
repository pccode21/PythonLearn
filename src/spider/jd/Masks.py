'''
 jd旗舰店检查到货
'''

import requests
import time
import smtplib  # smtplib 用于邮件的发信动作
from email.mime.text import MIMEText  # email 用于构建邮件内容
from email.header import Header  # 用于构建邮件头


# 有货通知 收件邮箱
mail = 'pccode21@gmail.com'
# 商品的url
url = [
    'https://c0.3.cn/stock?skuId=100011293950&area=19_1709_20093_51445&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=297418411&ch=1&callback=jQuery9224214',
    'https://c0.3.cn/stock?skuId=100006248245&area=19_1709_20093_51445&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=297418411&ch=1&callback=jQuery9224214',
    'https://c0.3.cn/stock?skuId=29054001796&area=19_1709_20093_51445&venderId=672329&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=297418411&ch=1&callback=jQuery753249',
    'https://c0.3.cn/stock?skuId=100011293952&area=19_1709_20093_51445&venderId=1000078145&buyNum=1&choseSuitSkuIds=&cat=9192,12190,1517&extraParam={%22originid%22:%221%22}&fqsp=0&pdpin=&pduid=297418411&ch=1&callback=jQuery9224214']


def sendMail(url):
    # 发信方的信息：发信邮箱，QQ 邮箱授权码
    from_addr = '16007005@qq.com'
    password = 'gjdhzzwvaxeecahc'

    # 收信方邮箱
    to_addr = mail

    # 发信服务器
    smtp_server = 'smtp.qq.com'

    # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    msg = MIMEText(url + ' 有口罩啦', 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(from_addr)
    msg['To'] = Header(to_addr)
    msg['Subject'] = Header('有口罩啦')

    # 开启发信服务，这里使用的是加密传输
    # 因为Python 3.7修改了ssl.py，导致smtplib.SMTP_SSL也连带产生了问题
    # 在括号内加入host参数"smtp_server"
    server = smtplib.SMTP_SSL(smtp_server)
    server.connect(smtp_server, 465)
    # 登录发信邮箱
    server.login(from_addr, password)
    # 发送邮件
    server.sendmail(from_addr, to_addr, msg.as_string())
    # 关闭服务器
    server.quit()


while (1):
    try:
        session = requests.Session()
        session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Accept": "*/*",
            "Connection": "keep-alive"
        }
        for i in url:
            # 商品url
            skuidUrl = 'https://item.jd.com/'+i.split('skuId=')[1].split('&')[0]+'.html'
            response = session.get(i)
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            if (response.text.find('无货') > 0):
                print('无货 ： ' + skuidUrl)
            else:
                print('有货啦! 有货啦! 有货啦! ： ' + skuidUrl)
                sendMail(skuidUrl)

            time.sleep(3)
    except Exception as e:
        print(e)
        time.sleep(3)
