import os
import math
import PIL.Image as Image  # 图像处理库PIL的Image模块
from wxpy import Bot

os.chdir(r'.\PythonLearn\src\spider\weixin')  # 指定工作路径


def mergeImage():
    print("正在合成头像")
    # 对用户头像进行压缩
    photo_width = 200
    photo_height = 200
    photo_path_list = []  # 图像路径list
    dirName = os.getcwd()+'/info/心境/images'  # 获取当前路径
    # 遍历文件夹获取所有图片的路径
    for root, dirs, files in os.walk(dirName):
        # os.walk是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情
        # 一个三元组(root,dirs,files)
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
        for file in files:
            if 'jpg' in file and os.path.getsize(os.path.join(root, file)) > 0:
                # os.path.join()在拼接路径的时候用的，在此是拼接root和file
                # os.path.getsize(path)返回文件大小（字节为单位），如果文件不存在就返回错误
                photo_path_list.append(os.path.join(root, file))
            elif 'jpg' in file and os.path.getsize(os.path.join(root, file)) == 0:
                photo_path_list.append(os.path.join('source', 'empty.jpg'))
                # 如果原有头像文件大小为0，就用文件夹‘source’下面的空白图片文件‘empty.jpg’代替
    pic_num = len(photo_path_list)  # 获取图像路径列表中的图像数量
    line_max = int(math.sqrt(pic_num))  # 每列显示图片数量，math.sqrt(pic_num)返回图像数量的平方根
    row_max = int(math.sqrt(pic_num))  # 每行显示图片数量，math.sqrt(pic_num)返回图像数量的平方根
    # 在此处，line_max == row_max，说明合成的图像是由行和列显示的图片数量相同的正方形图形
    print(line_max, row_max, pic_num)  # 打印合成图像的列图片数量、行图片数量和图片总数
    # print(math.sqrt(295))  # 结果是：17.175564037317667
    if line_max > 20:  # 由于图片合成的顺序为先列后行，所以要根据列的数量来判断
        line_max = 20  # 设定每列最多显示图片数量为20
        row_max = 20  # 设定每行最多显示图片数量为20
    num = 0
    pic_max = line_max*row_max  # 合成的图像里面的图片数量=每列最多显示图片数量 * 每行最多显示图片数量
    toImage = Image.new('RGB', (photo_width*line_max, photo_height*row_max))  # 生成新的图像
    # 保存成‘PNG’图片，使用‘RGBA’；保存成‘JPG’图片，使用‘RGB’
    # Image.new(mode,size)，size是给定的宽/高二元组，这是按照像素数来计算的。
    # 宽=photo_width*line_max,每张压缩后的头像图片宽度*每列最多显示图片数量
    # 高=photo_height*row_max,每张压缩后的头像图片高度*每行最多显示图片数量
    for i in range(0, row_max):  # 1=<row_max<=20
        for j in range(0, line_max):  # 1=<line_max<=20
            pic_file_head = Image.open(photo_path_list[num])
            # Image.open(file)，打开并确认给定的图像文件。这个是一个懒操作；该函数只会读文件头，而真实的图像数据直到试图处理该数据才会从文件读取
            # 可以使用一个字符串（表示文件名称的字符串）或者文件对象作为变量file的值
            width, height = pic_file_head.size  # size是给定的宽/高二元组，这是按照像素数来计算的
            fromImage = pic_file_head.resize((photo_width, photo_height))  # 调整图片的尺寸(宽，高)
            coordinate = (int(j % row_max * photo_width), int(i % row_max * photo_height))  # 坐标系（X,Y）,先列后行
            toImage.paste(fromImage, coordinate)  # 把图片贴进来，坐标系，左上角是(0,0)
            num = num+1
            if num >= len(photo_path_list):  # 用来判断贴进来的图片数量是否已经超过图像路径列表中的图像数量
                break
        if num >= pic_max:  # 用来判断贴进来的图片数量是否已经超过合成的图像里面的图片数量
            break
    print(toImage.size)  # 打印合成图片的尺寸,（17*200=3400,17*200=3400）
    toImage.save('analyse/merged.jpg')


if __name__ == '__main__':
    # 头像合成
    mergeImage()
    # bot = Bot()
    # bot.file_helper.send_image(path=r'.\analyse\merged.jpg')
