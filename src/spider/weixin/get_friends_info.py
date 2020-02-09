from wxpy import Bot, embed  # 微信机器人
import os
import codecs
import json

sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"
message_dict = {
    '手气最佳': '更多好玩的内容请关注朋友圈',
    '你好': '你好啊，这条消息是自动回复的',
    '备忘录': '这周开始早上要记得在部门群里上班打卡'}


def download_images(friend_list):  # 下载好友头像
    image_dir = 'info/' + bot.self.name + '/images/'
    for myfriend in friend_list:
        print('正在保存 %s 的头像...' % myfriend['NickName'])
        image_name = str(myfriend['NickName']) + '.jpg'
        img = bot.core.get_head_img(userName=myfriend["UserName"])
        with open(image_dir + image_name, 'wb') as file:
            file.write(img)


def save_data(frined_list):
    out_file_name = 'data/myfriends.json'
    with codecs.open(out_file_name, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(frined_list, ensure_ascii=False))


def print_content(msg):
    NickName = msg['User']['NickName']
    user = Bot.core.friends().search(name=NickName)[0]
    text = msg['Text']
    if text in message_dict.keys():
        user.send(message_dict[text])
    else:
        user.send(u"你好啊%s,我目前还不支持这个功能" % NickName)


if __name__ == '__main__':
    bot = Bot()
    os.chdir(r'.\PythonLearn\src\spider\weixin')  # 指定工作路径
    if not os.path.exists('info/' + bot.self.name):
        # 判断在‘weixin’文件下是否存在文件夹‘info’和机器人账号自身名称的文件夹
        filepath = os.getcwd()  # 获取工作路径
        os.makedirs(filepath + '/info/' + bot.self.name + '/images')
        # 在工作路径下创建文件夹‘info’、机器人账号自身名称的文件夹和‘images’文件夹
    myfriends = bot.core.get_friends(update=True)[0:]  # 获取微信好友列表
    myfriends_list = []
    for myfriend in myfriends:
        item = {}
        item['NickName'] = myfriend['NickName']
        item['HeadImgUrl'] = myfriend['HeadImgUrl']
        item['Sex'] = sex_dict[str(myfriend['Sex'])]
        item['Province'] = myfriend['Province']
        item['City'] = myfriend['City']
        item['Signature'] = myfriend['Signature']
        item['UserName'] = myfriend['UserName']
        myfriends_list.append(item)
        print(item)
    bot.file_helper.send('Hello from wxpy!')  # 向文件传输助手发送消息
    save_data(myfriends_list)
    download_images(myfriends_list)
    embed()  # 进入 Python 命令行、让程序保持运行
    # bot.join()  # 或者仅仅堵塞线程
