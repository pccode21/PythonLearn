import requests
from pyquery import PyQuery


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


def get_outer_list(MaxNum):
    list = []
    for i in range(1, MaxNum+1):
        url = 'https://gz.lianjia.com/ershoufang/pg'+str(i)
        print('正在爬取的链接为：%s'%url)
        response = requests.get(url, headers=headers)
        print('正在获取第 %d 页房源' % i)
        doc = PyQuery(response.text)
        num = 0
        for item in doc('.sellListContent li').items():
            num += 1
            list.append(item.attr('data-lj_action_housedel_id'))
        print('当前页面房源共 %s 套' % num)
    return list


def main():
    lists = get_outer_list(100)
    print('共计获取房源：',len(list(set(lists))))


if __name__ == '__main__':
    main()
