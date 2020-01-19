# encoding:UTF-8
import requests
from bs4 import BeautifulSoup


def get_teamlink(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
    res = requests.get(url, headers=headers)  # get方法中加入请求头
    res.encoding = 'utf-8'  # 设置编码格式防止乱码
    soup = BeautifulSoup(res.text, 'lxml')  # 对返回的结果进行解析
    team = soup.select('a[href^="team.php?id"]')  # #匹配 href开头是"team.php?id"的值
    print(team)
    print(len(team))
    team_list = {}
    for x in range(len(team)):
        team_list[str(team[x].string)] = str('http://match.sports.sina.com.cn/football/'+team[x].attrs['href'])
        # 将球队名称和球队链接连接起来，'球队名称':'球队链接'
        print(team_list)
    return (team_list)


England = get_teamlink('http://match.sports.sina.com.cn/football/opta_rank.php?year=2019&lid=1')  # 英超联赛的球队链接获取
Spain = get_teamlink('http://match.sports.sina.com.cn/football/opta_rank.php?year=2019&lid=2')  # 西甲联赛的球队链接获取
Germany = get_teamlink('http://match.sports.sina.com.cn/football/opta_rank.php?year=2019&lid=3')  # 德甲联赛的球队链接获取
Italy = get_teamlink('http://match.sports.sina.com.cn/football/opta_rank.php?year=2019&lid=4')  # 意甲联赛的球队链接获取
French = get_teamlink('http://match.sports.sina.com.cn/football/opta_rank.php?year=2019&lid=5')  # 法甲联赛的球队链接获取
with open(r'./PythonLearn/src/spider/players/teamlinks.csv', 'w') as f:  # 把数据放到csv文件中
    [f.write('{0},{1}\n'.format(key, value)) for key, value in England.items()]
    [f.write('{0},{1}\n'.format(key, value)) for key, value in Spain.items()]
    [f.write('{0},{1}\n'.format(key, value)) for key, value in Germany.items()]
    [f.write('{0},{1}\n'.format(key, value)) for key, value in Italy.items()]
    [f.write('{0},{1}\n'.format(key, value)) for key, value in French.items()]
