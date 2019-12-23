import requests
def getlocalweather():
    url='https://restapi.amap.com/v3/weather/weatherInfo'
    key='9f5d863e1b5694dc5e37ece0ab5d19b8'
    data={'key':key,'city':445200}
    req=requests.post(url,data)
    info=dict(req.json())
    """
    dict()创建字典，从映射对象的字典data初始化的新字典
    Requests内置的 JSON 解码器，处理 JSON 数据
    """
    print(info)
    newinfo=info['lives'][0]
    print("你查询的当地天气信息如下：")
    print("省市：",newinfo['province']+newinfo['city'])
    print("城市：", newinfo['city'])
    print("编码：", newinfo['adcode'])
    print("天气：", newinfo['weather'])
    print("气温：", newinfo['temperature']+'℃')
    print("风向：", newinfo['winddirection'])
    print("风力：", newinfo['windpower'])
    print("湿度：", newinfo['humidity'])
    print("报告时间：", newinfo['reporttime'])
if __name__=='__main__':
    getlocalweather()