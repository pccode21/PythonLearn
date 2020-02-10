from wxpy import Bot, embed, ensure_one  # 微信机器人
import os
import codecs
import json

bot = Bot()
sex_dict = {}
sex_dict['0'] = "其他"
sex_dict['1'] = "男"
sex_dict['2'] = "女"
department_group = ensure_one(bot.groups().search('我们运维部'))
# 通常可用在查找聊天对象时，确保查找结果的唯一性，并直接获取唯一项
# 定位部门群
manager = ensure_one(department_group.search(nick_name='龙'))  # 定位部门经理,nick_name(精准名称)


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


@bot.register(department_group)  # 将部门经理的消息转发到文件传输助手
def forward_manager_message(msg):
    if msg.member == manager:
        msg.forward(bot.file_helper, prefix='部门领导发言')


if __name__ == '__main__':
    os.chdir(r'.\PythonLearn\src\spider\weixin')  # 指定工作路径
    if not os.path.exists('info/' + bot.self.name):
        # 判断在‘weixin’文件下是否存在文件夹‘info’和机器人账号自身名称的文件夹
        filepath = os.getcwd()  # 显示当前python脚本工作路径
        os.makedirs(filepath + '/info/' + bot.self.name + '/images')
        # 可生成多层递规目录，在工作路径下创建文件夹‘info’、机器人账号自身名称的文件夹和‘images’文件夹
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
