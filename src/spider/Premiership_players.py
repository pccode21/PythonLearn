import re
import requests
from lxml import etree
from pyquery import PyQuery


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}
team_list_url = 'http://zq.win007.com/cn/League/2019-2020/36.html'


def get_team_list(teamListURL):
    html = requests.get(url=teamListURL, headers=headers).text
    parse_html = etree.HTML(html)
    list = []
    tr_list = parse_html.xpath('//*[@id="div_Table1"]/tbody/tr')
    for tr in tr_list:
        href = tr.xpath('./td[2]/a').get_attribute('href')
        print(href)
        list.append(re.findall(r'\d{2}', href)[0])


def main():
    list = get_team_list(team_list_url)
    print(list)


if __name__ == '__main__':
    main()
