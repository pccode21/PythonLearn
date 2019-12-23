import shodan                                      #搜索引擎
SHODAN_API_KEY='HIYpOiPz6hZbetQvdPN0raaj91sb03Lb'  #初始化
api=shodan.Shodan(SHODAN_API_KEY)
result=api.search('tomcat')                        #查询tomcat主机数量
print(result['total'])
ip_str=api.host('59.110.244.199')                  #查询制定IP地址
print(ip_str['country_name'])
print(ip_str['country_code'])