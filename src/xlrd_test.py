import xlrd
workbook=xlrd.open_workbook('test.xlsx')
print(workbook.sheet_names())
print(workbook.sheet_by_name('1班'))
sheet1 = workbook.sheets()[0]
print(sheet1.nrows)
print(sheet1.ncols)
print(sheet1.row_values(1))
print(sheet1.col_values(2))