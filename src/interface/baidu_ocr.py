from aip import AipOcr
import os
print(os.getcwd())                          #获取当前工作目录路径
APP_ID='17892281'
API_KEY='ttsvTWp0cmQ9KUCHrUNaLDmO'
SECRET_KEY='XPBk44bF48358Gce5e5fOCVYBUWMITCU'
client=AipOcr(APP_ID, API_KEY, SECRET_KEY)  #初始化=AipOcr对象
def get_file_content(filePath):             #读取图片
    with open(filePath,'rb') as fp:  
        return fp.read()
    '''
           上面的with open(...) as ...语句是以下语句的简化写法，建议之后文件读写都用该写法
    try:
        fp=open(filePath,'rb')
        return fp.read()
    finally:
           if fp:
                fp.close()
    rb 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
    
    '''
def img_to_str(filePath):
    options={}                              #如果有可选参数    
    options["language_type"]="CHN_ENG"      #中英文混合
    options["detect_direction"] = "true"    #检测朝向
    options["detect_language"] = "true"     #是否检测语言
    options["probability"] = "false"        #是否返回识别结果中每一行的置信度
    result=client.basicGeneral(get_file_content(filePath), options)  #带参数调用通用文字识别
    if 'words_result' in result:            
        text=('\n'.join([w['words'] for w in result['words_result']]))
        '''
                     上面 这句话，也可以拆分成这样：
        key = []
        if 'words_result' in result:         #先把words_result的内容提取出来
           for w in result['words_result']:  #再把words里面的内容提取出来
              key.append(w['words'])
        print("\n".join(key))                  #然后用join进行拼接
        words是识别结果字符串
        words_result是定位和识别结果数组
        '\n’ 是用于连接的字符（换行符）
         join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
         w 表示写入模式
        '''
    fs=open('/eclipse-workspace/txt/baidu_ocr.txt','w+',encoding='utf-8')
    '''
          相对路径
          将提取的文字保存成*.txt文件
    w+ 表示读写模式
    Windows下面新建的文本文件默认的编码是gbk（Windows简体中文版的系统默认编码就是gbk），当把从网页上读取的内容写到文本文件里面去的时候，意味着把一个unicode的字符序列写入到一个编码是gbk的文件，最后就出错了，解决方法就是在打开一个文件的时候，指定文件的编码，让它以指定的编码utf-8打开：
    '''
    fs.write(text)
    fs.close()
    return text
if __name__=='__main__':
    filePath='/eclipse-workspace/pictures/Childhood_fun.jpg'  #相对路径
    print(img_to_str(filePath))
    print("识别完成!")