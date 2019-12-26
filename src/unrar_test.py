from unrar import rarfile
rar = rarfile.RarFile(r'.\PythonLearn\src\Files\操作系统和office注册.rar', mode='r')  # mode的值只能为'r'
rar.namelist()
rar.printdir()
rf_list = rar.namelist()  # 得到压缩包里所有的文件
print('rar文件内容', rf_list)

for f in rf_list:
    rar.extract(f, r'.\PythonLearn\src\Files')  # 循环解压，将文件解压到指定路径
