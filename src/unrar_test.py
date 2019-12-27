from unrar import rarfile
rar = rarfile.RarFile(r'.\PythonLearn\src\Files\操作系统和office注册.rar', mode='r')  # mode的值只能为'r'
rar.namelist()
rar.printdir()
rf_list = rar.namelist()  # 得到压缩包里所有的文件
print('rar文件内容', rf_list)

for f in rf_list:
    rar.extract(f, r'.\PythonLearn\src\Files')  # 循环解压，将文件解压到指定路径

# Python 本身不支持 rar 文件的解压，需要先安装相关依赖才可使用
# 安装 unrar 模块：pip install unrar
# 如果上面的步骤不能安装，那就到“https://pypi.org/”下载unrar的压缩包，
# 将压缩包解压到Python的Lib\site-packages文件夹下，然后使用“python setup.py build”和“python setup.py install”进行安装
# 下载安装 unrar library，网址：http://www.rarlab.com/rar/UnRARDLL.exe 按照默认安装路径安装
# 将安装后文件夹中的 X64 文件夹加入环境变量（默认路径为 C:\Program Files (x86)\UnrarDLL\x64）
# 将C:\Program Files (x86)\UnrarDLL和C:\Program Files (x86)\UnrarDLL\x64目录下的两个文件都改为unrar.dll和unrar.lib
# 系统变量中新建变量，变量名输入 UNRAR_LIB_PATH，变量值为 C:\Program Files (x86)\UnrarDLL\x64\unrar.dll
# （32位系统下的变量值为C:\Program Files (x86)\UnrarDLL\unrar.dll）
# 将 winrar 的目录下的 unrar.exe 复制到 Python 路径的 Scripts 文件夹下
# 重启编译软件
