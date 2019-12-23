import xlsxwriter
import datetime
workbook=xlsxwriter.Workbook('test1.xlsx')
sheet1=workbook.add_worksheet('test_sheet')
workformat=workbook.add_format()
workformat.set_bold(True)         #字体加粗
workformat.set_border(1)          #单元格边框宽度
workformat.set_align('left')      #对齐方式
workformat.set_num_format('0.00')  #格式化数据格式为小数点后两位
heads = ['', '语文','数学', '英语']
datas = [
    ['小明', 76, 85, 95],
    ['小红', 85, 58, 92],
    ['小王', 98, 96, 91]
]
sheet1.write_row('A1', heads, workformat)
sheet1.write_row('A2', datas[0], workformat)
sheet1.write_row('A3', datas[1], workformat)
sheet1.write_row('A4', datas[2], workformat)
format1=workbook.add_format({'num_format': 'yyyy-mm-dd/hh:mm:ss'})
sheet1.write_datetime('E5',datetime.datetime(2019,11,25,0,51,20),format1)
sheet1.insert_image('I6','trees.jpg') 
#insert_image(row, col, image[, options])
#row：行坐标，起始索引值为0；
#col：列坐标，起始索引值为0；
#image：string类型，是图片路径；
#options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'values': '=test_sheet!$B$2:$B$4'})
chart.add_series({'values': '=test_sheet!$C$2:$C$4'})
chart.add_series({'values': '=test_sheet!$D$2:$D$4'})
sheet1.insert_chart('A7', chart)
workbook.close()