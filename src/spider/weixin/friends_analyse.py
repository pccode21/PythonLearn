import os
import math
import PIL.Image as Image
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
        for file in files:
            if 'jpg' in file and os.path.getsize(os.path.join(root, file)) > 0:
                photo_path_list.append(os.path.join(root, file))
            elif 'jpg' in file and os.path.getsize(os.path.join(root, file)) == 0:
                photo_path_list.append(os.path.join('source', 'empty.jpg'))
    pic_num = len(photo_path_list)
    # 每行每列显示图片数量
    line_max = int(math.sqrt(pic_num))
    row_max = int(math.sqrt(pic_num))
    print(line_max, row_max, pic_num)  # 打印最大列、最大行和图片总数
    if line_max > 20:
        line_max = 20
        row_max = 20
    num = 0
    pic_max = line_max*row_max
    toImage = Image.new('RGB', (photo_width*line_max, photo_height*row_max))  # 如果是保存成‘PNG’图片，要使用‘RGBA’
    for i in range(0, row_max):
        for j in range(0, line_max):
            pic_fole_head = Image.open(photo_path_list[num])
            width, height = pic_fole_head.size
            tmppic = pic_fole_head.resize((photo_width, photo_height))
            loc = (int(j % row_max * photo_width), int(i % row_max * photo_height))
            toImage.paste(tmppic, loc)
            num = num+1
            if num >= len(photo_path_list):
                break
        if num >= pic_max:
            break
    print(toImage.size)  # 打印合成图片的尺寸
    toImage.save('analyse/merged.jpg')


if __name__ == '__main__':
    # 头像合成
    mergeImage()
    # bot = Bot()
    # bot.file_helper.send_image(path=r'.\analyse\merged.jpg')
