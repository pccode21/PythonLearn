import requests,csv 
def main():
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
    addres = input('请输入查询的城市：')
    csvrow1=[]
    csvrow2=[]
    for page in range(1, 50):
        data = {
            'cname': addres,
            'pid': '',
            'pageIndex': str(page),
            'pageSize': "10",
            } 
        res = requests.post(url=url, headers=headers, data=data).json()
        data_detali = res.get('Table1') 
        content = {'店名':None,'地址':None}     
        for store in data_detali:
            storename = store.get('storeName')           # 获取店名
            storeaddress = store.get('addressDetail')    # 获取店地址
            content['店名'] = storename
            content['地址'] = storeaddress
            print(content)        
            csvrow1.append(storename)
            csvrow2.append(storeaddress) 
            with open('kfc.csv','w',newline='',encoding='utf-8-sig') as fp:  
                '''
                'w'打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
                                            存储数据
                 csv标准库中的writerow在写入文件时会加入'\r\n'作为换行符，if newline is ''，换行符不会被转化而是直接输出
                 “uft-8-sig"中sig全拼为 signature 也就是"带有签名的utf-8”, 因此"utf-8-sig"读取带有BOM的"utf-8文件时"会把BOM单独处理,与文本内容隔离开                           
                '''
#                json.dump(content, fp,ensure_ascii=False)     #使用ensure_ascii=False后，写入中文不会乱码
                writer = csv.writer(fp)
                header=['店名','地址']
                writer.writerow(header)            
                writer.writerows(zip(csvrow1,csvrow2))  ##zip() 函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
                fp.close()
if __name__ == '__main__':
    main()