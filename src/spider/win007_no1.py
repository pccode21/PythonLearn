import requests
import time
import re
import pymysql
import traceback

url_time = time.strftime('%Y%m%d%H%M%S')
# 获取带有时间的url
url = 'http://zq.win007.com/jsData/matchResult/2019-2020/s36.js?version='+url_time
# 需要加入跳转网页
headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'zq.win007.com',
            'Referer': 'http://zq.win007.com/cn/League/2019-2020/36.html',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
            'Cookie': 'bfWin007FirstMatchTime=2020,0,7,08,00,00; win007BfCookie=0^0^1^1^1^1^1^0^0^0^0^0^1^2^1^1^0^1^1^0; UM_distinctid=16f82dd359f17e-0864fb7189f26a-c383f64-100200-16f82dd35a1123; CNZZDATA1261430177=958542710-1578443893-http%253A%252F%252Fzq.win007.com%252F%7C1578465496'
            }
# 解析网站
time.sleep(3)
l = 0
try:
    # get请求可以使用status_code查看访问是否正常
    response1 = requests.get(url, headers=headers).status_code
    # 判断网站的正常
    if response1 == 200:
        s = requests.session()
        s.keep_alive = False
        resp = requests.get(url, headers=headers)
        # print(resp.text)
        # 获取球队ID
        pattern = 'var arrTeam =(.*?);'
        res = re.search(pattern, resp.text).group(1)
        res = eval(res)
        team_id_list = []
        time.sleep(2)
        for i in res:
            team_id = i[0]
            team_id_list.append(team_id)
        time.sleep(2)
        # 取出id 并写入url，跳转球队信息页
        for i in team_id_list:
            # 出现异常提示未存入
            time.sleep(3)
            headers = {
                'Referer': 'http://zq.win007.com/cn/team/Summary/{}.html'.format(i),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
            }
            try:
                url_qd = 'http://zq.win007.com/jsData/teamInfo/' \
                          'teamDetail/tdl{}.js?version={}'.format(i, url_time)
                response1 = requests.get(url_qd, headers=headers).status_code
                if response1 == 200:
                    s = requests.session()
                    s.keep_alive = False
                    res_qd = requests.get(url_qd, headers=headers)
                    l = l+1
                    # 解析数据球队信息,并存入字典
                    result = {}
                    pattern = "var teamCharacter =(.*);"
                    res_age = re.search(pattern, res_qd.text).group(1)
                    res_age = eval(res_age)
                    ys = []
                    fg = []
                    rd = []
                    for i in res_age:
                        if i[0] == 1:
                            ys.append(i[2])
                        elif i[0] == 2:
                            fg.append(i[2])
                        elif i[0] == 3:
                            rd.append(i[2])
                    pattern = 'var teamDetail =(.*)'
                    res_team = re.findall(pattern, res_qd.text)
                    pattern = 'var coach =(.*?);'
                    res_chief = re.search(pattern, res_qd.text).group(1).split(',')
                    for y in res_team:
                        res_team = y.split(',')
                        result['qd_name'] = res_team[1]
                        result['yy_name'] = res_team[2]
                        result['el_name'] = res_team[3]
                        result['thecity'] = res_team[5]
                        result['home_field'] = res_team[8]
                        result['set_up'] = res_team[12]
                        result['coach'] = res_chief[2]
                        result['address'] = res_team[13]
                        result['website'] = res_team[-1]
                        result['ys'] = ys
                        result['fg'] = fg
                        result['rd'] = rd
                        print('已将{}球队信息存入..'.format(result['qd_name']))
                        # 打开数据库
                        connect = pymysql.connect('localhost', 'root', 'Lxd05230708', 'football')
                        # 创建游标
                        conn = connect.cursor()
                        # 添加数据
                        insert_sql = 'insert into team_stats(qd_name, yy_name, el_name, thecity, home_field, set_up, coach, address, website, ys, fg, rd)' \
                                 ' values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (
                                     result['qd_name'], result['yy_name'],result['el_name'],
                                     result['thecity'],result['home_field'],result['set_up']
                                     ,result['coach'] ,result['address'] ,result['website'],
                                     result['ys'],result['fg'],result['rd'])
                        # 执行语句
                        conn.execute(insert_sql)
                        # 执行事务
                        connect.commit()
                        # 关闭数据库
                        connect.close()
                        # 关闭游标
                        conn.close()
            except:
                if traceback.format_exc():
                    print('丢失球员{}的数据'.format(result['qd_name']))
        else:
            print('未进入到球队信息页')
    else:
        print('未进入到球队列表页')
except:
    if traceback.format_exc():
        print('丢失数据')
