#coding=utf-8
import requests
import string
import csv
import re
import codecs

r = requests.get('http://zq.win007.com/jsData/teamInfo/teamDetail/tdl1419.js')
tmp = r.content
m = re.findall(r"(\[\d{7}.*.\];)", tmp.decode("utf-8"))[0]
m = m.split('],[')
for i in m:
    i = re.sub(r"\^.*?'", "", i)
    i = re.sub(r"[\]\[;\']", "", i)
    i = re.sub(r"#[0-9A-Za-z]{6},", "", i)
    i = re.sub(r"\d{7},", "", i)
    with open('test.csv', 'a+') as f:
        f.write(codecs.BOM_UTF8)
        f_csv = csv.writer(f)
        tmp = i.split(",")
        f_csv.writerow(tmp)
