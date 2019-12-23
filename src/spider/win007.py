import requests
url='http://vip.win007.com/changeDetail/handicap.aspx?id=1740612&companyid=8&l=0'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
html_content=requests.get(url=url,headers=headers).text
print(html_content)