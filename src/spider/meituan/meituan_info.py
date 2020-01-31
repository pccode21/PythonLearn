import csv
import time
import requests
import json


# 区域店铺id ct_Poi cateName抓取，传入参数为区域id
def get_id(areaid):
    id_list = []
    url = 'http://meishi.meituan.com/i/api/channel/deal/list'
    headers = {'Host': 'meishi.meituan.com',
                'Accept': 'application/json',
                'Referer': 'http://meishi.meituan.com/i/',
                'Cookie': '__mta=250894649.1579801629158.1580402333879.1580402515416.14; iuuid=0D7D6F593011EB86E6F59602C319A9D602C897BADCACCFDC1C4BD97B8EB11CDF; cityname=%E6%8F%AD%E9%98%B3; _lxsdk_cuid=16fd36ab7a5c8-0b01d2d9831789-33365a01-100200-16fd36ab7a5c8; _lxsdk=0D7D6F593011EB86E6F59602C319A9D602C897BADCACCFDC1C4BD97B8EB11CDF; webp=1; __utma=74597006.1817794631.1579799985.1579799985.1579799985.1; __utmz=74597006.1579799985.1.1.utmcsr=blog.csdn.net|utmccn=(referral)|utmcmd=referral|utmcct=/xing851483876/article/details/81842329; _lx_utm=utm_source%3Dblog.csdn.net%26utm_medium%3Dreferral%26utm_content%3D%252Fxing851483876%252Farticle%252Fdetails%252F81842329; _hc.v=cfdc472c-7aed-9b3b-bc3b-68b5742b7713.1579800858; a2h=2; i_extend=C189913015384320739764905118182476349850_b1_c0_e86901326389387811304GimthomepageallcateH__a100265__b1; latlng=23.512963,116.355181,1579801553690; ci=288; client-id=db2d3ca3-cf63-45d5-a163-ae5a4bfedebc; uuid=b5957ea9-12eb-49be-ad53-4093607fcfba; logan_custom_report=; logan_session_token=q9lltqmxcddel3ynp2jl; _lxsdk_s=16ff72652a6-f2b-aba-ec0%7C%7C27',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
            }
    data = {"uuid": "b5957ea9-12eb-49be-ad53-4093607fcfba",
            "version": "8.3.3",
            "platform": 3,
            "app": "",
            "partner": 126,
            "riskLevel": 1,
            "optimusCode": 10,
            "originUrl": "http://meishi.meituan.com/i/",
            "offset": 0,
            "limit": 15,
            "cateId": 1,
            "lineId": 0,
            "stationId": 0,
            "areaId": 0,
            "sort": "default",
            "deal_attr_23": "",
            "deal_attr_24": "",
            "deal_attr_25": "",
            "poi_attr_20043": "",
            "poi_attr_20033": ""
            }
    r = requests.post(url=url, headers=headers, data=data)
    result = json.loads(r.text)
    print(result)
    totalcount = result['data']['poiList']['totalCount']  # 获取该分区店铺总数，计算出要翻的页数
    datas = result['data']['poiList']['poiInfos']
    print(len(datas), totalcount)
    for d in datas:
        d_list = ['', '', '', '']
        d_list[0] = d['name']
        d_list[1] = d['cateName']
        d_list[2] = d['poiid']
        d_list[3] = d['ctPoi']
        id_list.append(d_list)
    print('Page：1')
    # 将数据保存到本地csv
    with open(r'./PythonLearn/src/spider/meituan/meituan_id.csv', 'a', newline='', encoding='gb18030') as f:
        write = csv.writer(f)
        for i in id_list:
            write.writerow(i)

    # 开始爬取第2页到最后一页
    offset = 0
    if totalcount > 15:
        totalcount -= 15
        while offset < totalcount:
            id_list = []
            offset += 15
            m = offset/15+1
            print('Page:%d' % m)
            # 构造post请求参数，通过改变offset实现翻页
            data2 = {"uuid": "b5957ea9-12eb-49be-ad53-4093607fcfba",
                    "version": "8.3.3",
                    "platform": 3,
                    "app": "",
                    "partner": 126,
                    "riskLevel": 1,
                    "optimusCode": 10,
                    "originUrl": "http://meishi.meituan.com/i/",
                    "offset": offset,
                    "limit": 15,
                    "cateId": 1,
                    "lineId": 0,
                    "stationId": 0,
                    "areaId": areaid,
                    "sort": "default",
                    "deal_attr_23": "",
                    "deal_attr_24": "",
                    "deal_attr_25": "",
                    "poi_attr_20043": "",
                    "poi_attr_20033": ""
                    }
            try:
                r = requests.post(url=url, headers=headers, data=data2)
                print(r.text)
                result = json.loads(r.text)
                print(result)
                datas = result['data']['poiList']['poiInfos']
                print(len(datas))
                for d in datas:
                    d_list = ['', '', '', '']
                    d_list[0] = d['name']
                    d_list[1] = d['cateName']
                    d_list[2] = d['poiid']
                    d_list[3] = d['ctPoi']
                    id_list.append(d_list)
                # 保存到本地
                with open(r'./PythonLearn/src/spider/meituan/meituan_id.csv', 'a', newline='', encoding='gb18030') as f:
                    write = csv.writer(f)
                    for i in id_list:
                        write.writerow(i)
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    # 直接将html代码中区域的信息复制出来，南澳新区的数据需要处理下，它下面没有分区
    a = {"areaObj":{"3650":[{"id":3650,"name":"全部","regionName":"榕城区","count":588},
                            {"id":12388,"name":"金城步行街","regionName":"金城步行街","count":21},
                            {"id":12389,"name":"进贤门","regionName":"进贤门","count":9},
                            {"id":12390,"name":"仁港商业街","regionName":"仁港商业街","count":27},
                            {"id":12391,"name":"江南新城","regionName":"江南新城","count":24},
                            {"id":12614,"name":"广百百货","regionName":"广百百货","count":18},
                            {"id":14219,"name":"渔湖镇","regionName":"渔湖镇","count":30},
                            {"id":14220,"name":"同德路","regionName":"同德路","count":4},
                            {"id":14221,"name":"东一路","regionName":"东一路","count":15},
                            {"id":14223,"name":"一号路","regionName":"一号路","count":12},
                            {"id":14224,"name":"榕华大道","regionName":"榕华大道","count":14},
                            {"id":14225,"name":"学宫广场","regionName":"学宫广场","count":8},
                            {"id":14226,"name":"女人街","regionName":"女人街","count":5},
                            {"id":14227,"name":"望江北路","regionName":"望江北路","count":18},
                            {"id":14228,"name":"东二路","regionName":"东二路","count":15},
                            {"id":14240,"name":"黄岐山大道","regionName":"黄岐山大道","count":11},
                            {"id":14241,"name":"马牙路","regionName":"马牙路","count":17},
                            {"id":14242,"name":"揭阳楼","regionName":"揭阳楼","count":""},
                            {"id":14254,"name":"八号街","regionName":"八号街","count":27},
                            {"id":14256,"name":"宝德广场","regionName":"宝德广场","count":5},
                            {"id":14273,"name":"二号路","regionName":"二号路","count":14},
                            {"id":14283,"name":"市政府","regionName":"市政府","count":13},
                            {"id":15420,"name":"炮台镇","regionName":"炮台镇","count":29},
                            {"id":27064,"name":"梅云镇","regionName":"梅云镇","count":6},
                            {"id":34774,"name":"揭东潮汕机场","regionName":"揭东潮汕机场","count":1},
                            {"id":36382,"name":"揭阳潮汕国际机场","regionName":"揭阳潮汕国际机场","count":4},
                            {"id":36411,"name":"榕江一品风情街","regionName":"榕江一品风情街","count":7},
                            {"id":36624,"name":"揭阳学院","regionName":"揭阳学院","count":1}],
                    "3651":[{"id":3651,"name":"全部","regionName":"普宁市","count":368},
                            {"id":13048,"name":"万泰汇","regionName":"万泰汇","count":37},
                            {"id":13049,"name":"广达美佳乐","regionName":"广达美佳乐","count":14},
                            {"id":13050,"name":"国际商品城","regionName":"国际商品城","count":33},
                            {"id":13051,"name":"新河路","regionName":"新河路","count":16},
                            {"id":13053,"name":"环城南路","regionName":"环城南路","count":19},
                            {"id":13054,"name":"普宁二中","regionName":"普宁二中","count":28},
                            {"id":13055,"name":"兰花广场","regionName":"兰花广场","count":20},
                            {"id":36625,"name":"星河COCO City","regionName":"星河COCO City","count":32}],
                    "3652":[{"id":3652,"name":"全部","regionName":"揭东区","count":208},
                            {"id":14218,"name":"金溪大道","regionName":"金溪大道","count":25},
                            {"id":19572,"name":"阳美","regionName":"阳美","count":37},
                            {"id":27063,"name":"霖磐镇","regionName":"霖磐镇","count":16},
                            {"id":37487,"name":"埔田镇","regionName":"埔田镇","count":17}],
                    "3653":[{"id":3653,"name":"全部","regionName":"揭西县","count":24},
                            {"id":20784,"name":"华茂综合商店","regionName":"华茂综合商店","count":""},
                            {"id":20791,"name":"霖都大道","regionName":"霖都大道","count":11}],
                    "3654":[{"id":3654,"name":"全部","regionName":"惠来县","count":30},
                            {"id":20724,"name":"南环一路","regionName":"南环一路","count":3},
                            {"id":20728,"name":"消防路","regionName":"消防路","count":11}]
                    }}
    datas = a['areaObj']
    b = datas.values()
    area_list = []
    for data in b:
        for d in data[1:]:
            area_list.append(d)  # 将每个区域信息保存到列表，元素是字典
    l = 0
    old = time.time()
    for i in area_list:
        l += 1
        print('开始抓取第%d个区域：'%l, i['regionName'], '店铺总数：', i['count'])
        try:
            get_id(i['id'])
            now = time.time()-old
            print(i['name'], '抓取完成！', '时间:%d' % now)
        except Exception as e:
            print(e)
            continue
