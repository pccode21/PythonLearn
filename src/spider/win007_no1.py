# 导入需要的包
from selenium import webdriver
import time
import traceback


# 发送url请求
def getDriver(url):
    try:
        # 注意chromedriver的版本
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(1)
        return driver
    except:
        return ''


# 获取子链接列表
def getURLlist(url, teamURLlist):
    driver = getDriver(url)
    try:
        # 找到包含子链接的所有a标签
        a_list = driver.find_elements_by_xpath('//table[@id="ScoreGroupTab"]/tbody/tr/td[2]/a')
        if a_list:
            for i in a_list:
                # teamURLlist用于存放子链接
                teamURLlist.append(i.get_attribute('href'))
            driver.close()
            return teamURLlist
        else:
            return []
    except:
        traceback.print_exc()
        return []


# 获取比赛数据
def getMatchInfo(teamURLlist, fpath):
    with open(fpath, 'w') as f:
        # 注意逗号后面不要有空格
        f.write('比赛,时间,主队,比分,客队,犯规,黄牌,红牌,控球率,射门（射正）,传球（成功）,传球成功率,过人次数,评分\n')
        if teamURLlist:
            for url in teamURLlist:
                driver = getDriver(url)
                # 表格中数据数据分了好多页，虽然所有数据在driver.page_source中都可见。
                # 但是，除第一页以外，其他的数据style属性都是“display:none",selenium对这些元素是无法直接操作的。
                # 我们需要通过JavaScipt 修改display的值

                # 编写一段javascript代码，让浏览器执行。从而把html中的所有tr标签的style属性都设为display='block'
                js = 'document.querySelectorAll("tr").forEach(function(tr){tr.style.display="block";})'
                driver.execute_script(js)

                # 接下来，就可以把所有的比赛成绩数据都爬下来
                infolist = driver.find_elements_by_xpath('//div[@id="Tech_schedule"]/table/tbody/tr')

                # 第一个tr中包含的是表格的title信息，剔除
                for tr in infolist[1:]:
                    td_list = tr.find_elements_by_tag_name('td')
                    matchinfo = []
                    for td in td_list:
                        # 部分td的style属性也为“display:none"，info 则对应为‘’，
                        # 这些td对应的是角球，越位，头球，救球，铲球等信息，不是很重要，就不爬取了。
                        info = td.text
                        if info:  # 去除空字符
                            matchinfo.append(td.text)
                            matchinfo.append(',')    # 添加逗号作为分隔符
                    matchinfo.append('\n')  # 在列表最后加上换行符

                    # 将一条比赛信息写入到文件中
                    f.writelines(matchinfo)

                # 每个网页爬完后，就把打开的浏览器关掉，要不最后会开着好多浏览器窗口。
                driver.close()


def main():
    # 一级网址：32强分组信息
    start_url = 'http://zq.win007.com/cn/CupMatch/75.html'
    # 保存文件及路径
    output = r'.\PythonLearn\src\spider\worldcup2018.csv'
    startlist = []
    resultlist = getURLlist(start_url, startlist)
    print(resultlist)
    getMatchInfo(resultlist, output)
    print('\nfinished\n')


if __name__ == '__main__':
    main()
