import tkinter
import tkinter.filedialog
import os
import zipfile
import tkinter.messagebox
from PIL import ImageTk, Image

# 创建住窗口
root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=700, height=500, bd=0)
root.title('足球心经的压缩软件')
root.iconbitmap(r'.\PythonLearn\src\images\LOGO.ico')
imgpath = r'.\PythonLearn\src\images\green.jpg'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
canvas.create_image(700, 500, image=photo)
canvas.pack()


# 声明一个全局变量files
files = ()
# 声明lable的使用变量
filenames = tkinter.StringVar()


# 1.选取文件操作
def selecfiles():
    # 声明全局变量
    global files
    # 使用文件对话框选择文件
    files = tkinter.filedialog.askopenfilenames(title='选择你要要做的软件bitch')
    # 显示选中文件的信息
    # 临时的路径容器
    tmpfiles = []
    for i in files:
        if len(i) > 60:
            i = i[0:20] + '...' + i[-15:]
        tmpfiles.append(i)
    filestr = '\n'.join(tmpfiles)
    print(filestr)
    filenames.set(filestr)                                    # 在标签中显示文件名称


# 2.压缩文件函数
def zipfiles():
    global files
    # 获取压缩文件的路径
    filename = tkinter.filedialog.asksaveasfilename(title='保存文件', filetypes=(('zip 文件', '*.zip'), ('所有文件', '*.*')))
    # 新建压缩文件
    zp = zipfile.ZipFile(filename + '.zip', 'a')              # 压缩文件默认zip格式
    # 添加要压缩的文件(遍历操作
    for onefiles in files:
        zp.write(onefiles, os.path.basename(onefiles))
    zp.close()  # 创建完成
    # 提示用户压缩路径
    tkinter.messagebox.showinfo(title='操作结果', message='压缩成功：' + filename)


# 3.解压操作函数
def uncompress():
    global files

    # 使用文件对话框选择文件
    files = tkinter.filedialog.askopenfilenames(title='选择你要要做的软件bitch')
    # 显示选中文件的信息
    # 临时的路径容器
    tmpfiles = []
    for i in files:
        if len(i) > 60:
            i = i[0:20] + '...' + i[-15:]
        tmpfiles.append(i)
    filestr = '\n'.join(tmpfiles)
    print(filestr)
    filenames.set(filestr)

    zp = zipfile.ZipFile(filestr, 'r')
    # 添加要压缩的文件(遍历操作
    # for onefiles in files:
    files1 = tkinter.filedialog.askdirectory(title='选择您要解压的路径')
    zp.extractall(files1)
    zp.close()  # 解压完成
    # 提示用户压缩路径
    tkinter.messagebox.showinfo(title='操作结果', message='解压成功：'+files1)


# 界面布局
# 菜单栏
allmenu = tkinter.Menu(root)

filmenu = tkinter.Menu(allmenu, tearoff=0)
filmenu.add_command(label='打开')
filmenu.add_command(label='保存')
filmenu.add_separator()
filmenu.add_command(label='设置')
filmenu.add_command(label='退出')

filmenu1 = tkinter.Menu(allmenu, tearoff=0)
filmenu1.add_command(label='打开')
filmenu1.add_command(label='保存')
filmenu1.add_separator()
filmenu1.add_command(label='设置')
filmenu1.add_command(label='退出')


allmenu.add_cascade(label='文件', menu=filmenu)
allmenu.add_cascade(label='编辑', menu=filmenu1)
allmenu.add_cascade(label='工具')

root.config(menu=allmenu, bg='black')


# 添加按钮界面
# label = tkinter.Label(root, bg='#242424')
# label.place(width=700, height=115)

# 1.添加文件按钮
btnadd = tkinter.Button(root, text='选择文件', bg='#242424', bd=0.5, fg='grey', command=selecfiles)
# btnadd.place(x=100, y=70, width='80', height=30)
btnadd.pack()
canvas.create_window(110, 70, width=80, height=30, window=btnadd)

# 2.压缩操作按钮
btnadd = tkinter.Button(root, text='压缩文件', bg='#242424', bd=0.5, fg='grey', command=zipfiles)
# btnadd.place(x=300, y=70, width='80', height=30)
btnadd.pack()
canvas.create_window(310, 70, width=80, height=30, window=btnadd)

# 3.解压操作按钮
btnadd = tkinter.Button(root, text='解压文件', bg='#242424', bd=0.5, fg='grey', command=uncompress)
# btnadd.place(x=500, y=70, width='80', height=30)
btnadd.pack()
canvas.create_window(510, 70, width=80, height=30, window=btnadd)

img1 = tkinter.PhotoImage(file=r'.\PythonLearn\src\images\choice.gif')
labelg1 = tkinter.Label(root, image=img1)
# labelg1.place(x = 115,y =15,width = 50,height = 50)
labelg1.pack()
canvas.create_window(115, 30, width=50, height=50, window=labelg1)

img2 = tkinter.PhotoImage(file=r'.\PythonLearn\src\images\zip.gif')
labelg2 = tkinter.Label(root, image=img2)
# labelg2.place(x = 317,y =15,width = 50,height = 50)
labelg2.pack()
canvas.create_window(317, 30, width=50, height=50, window=labelg2)

img3 = tkinter.PhotoImage(file=r'.\PythonLearn\src\images\gunzip.gif')
labelg3 = tkinter.Label(root, image=img3)
# labelg3.place(x = 515,y =15,width = 50,height = 50)
labelg3.pack()
canvas.create_window(515, 30, width=50, height=50, window=labelg3)

# 4显示信息的组件
label = tkinter.Label(root, textvariable=filenames, anchor='nw', justify='left')
label.pack()
# label.place(x= 5,y = 115,width = '690',height = '370')
canvas.create_window(100, 300, width=200, height=100, window=label)


root.mainloop()
