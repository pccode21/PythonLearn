import requests
from lxml import etree
import pymysql
import re


class GovementSpider(object):
    def __init__(self):
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
        }
        self.db = pymysql.connect('localhost', 'root', 'Lxd05230708', 'spider', charset='utf8')
        self.cursor = self.db.cursor()

    # 提取二级页面链接(假链接)
    def get_false_link(self):
        html = requests.get(url=self.one_url, headers=self.headers).content.decode('utf-8', 'ignore')
        parse_html = etree.HTML(html)
        # xpath://a[@class='artitlelist']
        r_list = parse_html.xpath("//a[@class='artitlelist']")
        for r in r_list:
            # 或者这么找title属性值
            # title = r.get('title')
            title = r.xpath("./@title")[0]
            # 利用正则找到第一个自己需要的title里面的地址(第一个一般都是最新的)
            if re.findall(r'.*?中华人民共和国县以上行政区划代码.*?', title, re.RegexFlag.S):
                # 获取到第1个就停止即可，第1个永远是最新的链接
                two_link = 'http://www.mca.gov.cn' + r.xpath('./@href')[0]
                return two_link

    # 提取真是的二级页面链接(返回数据的链接)
    def get_true_link(self):
        two_false_link = self.get_false_link()
        html = requests.get(url=two_false_link, headers=self.headers).text
        pattern = re.compile(r'window.location.href="(.*?)"', re.RegexFlag.S)
        real_link = pattern.findall(html)[0]
        self.get_data(real_link)

    # 真正提取数据函数
    def get_data(self, real_link):
        html = requests.get(url=real_link, headers=self.headers).text
        # 基本xpath: //tr[@height="19"]
        parse_html = etree.HTML(html)
        tr_list = parse_html.xpath('//tr[@height="19"]')
        for tr in tr_list:
            # code: ./td[2]/text()
            code = tr.xpath('./td[2]/text()')[0]
            # name: ./td[3]/text()
            name = tr.xpath('./td[3]/text()')[0]
            print(code, name)
            self.save_sql(code, name)

    def save_sql(self, code, name):
            self.cursor.execute("insert into version values(default, '%s', '%s')" % (code, name))
            # 数据表中id要设置成 `id` INT NOT NULL AUTO_INCREMENT 和 PRIMARY KEY (`id`)
            self.db.commit()

    # 主函数
    def main(self):
        self.get_true_link()
        self.cursor.close()
        self.db.close()


if __name__ == "__main__":
    spider = GovementSpider()
    spider.main()
