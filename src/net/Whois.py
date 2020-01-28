import urllib.request
import whois
req_whois = urllib.request.urlopen('http://whois.chinaz.com/doucube.com')
print(req_whois.read().decode())
data = whois.whois('www.baidu.com')
print(data)
