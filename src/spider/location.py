import requests
def getlocation():
    url='https://restapi.amap.com/v3/geocode/geo'
    key='9f5d863e1b5694dc5e37ece0ab5d19b8'
    data={'key':key,'address':'潮汕机场航站楼商铺编号为一层D03','city':445200}
    req=requests.post(url,data)
    info=dict(req.json())
    """
    dict()创建字典，从映射对象的字典data初始化的新字典
    Requests内置的 JSON 解码器，处理 JSON 数据
    """
    print(info)
    newinfo=info['geocodes'][0]
    print("你查询的肯德基门店的经纬度信息如下：")
    print("地址编码：", newinfo['adcode'])
    print("经纬度：", newinfo['location'])
if __name__=='__main__':
    getlocation()