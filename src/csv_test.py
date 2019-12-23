import csv
import os

def main():

    current_dir = os.path.abspath('.')
    file_name = os.path.join(current_dir, "csss.csv")
    csvfile = open(file_name, 'wt' ,encoding="utf-8-sig",newline='')  #

    writer=csv.writer(csvfile, delimiter=",")
    header=['uel','title']
    csvrow1=[]
    csvrow2=[]
    csvrow1.append("测试1")
    csvrow1.append("测试2")
    csvrow2.append("111")
    csvrow2.append("222")

    writer.writerow(header)
    writer.writerows(zip(csvrow1,csvrow2))  #zip() 函数用于将可迭代对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象


    csvfile.close()

if __name__ == '__main__':
    main()