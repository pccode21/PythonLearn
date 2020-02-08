from wxpy import Bot, embed  # 微信机器人
import os
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
os.chdir(r'.\PythonLearn\src\images')  # 创建工作路径
bot = Bot()
myself = bot.self  # 机器人账号自身
# bot.file_helper.send('Hello from wxpy!')  # 向文件传输助手发送消息
# 若需要给自己发送消息，请先进行以下一次性操作:
# myself.add()  # 在 Web 微信中把自己加为好友
# myself.accept()
# myself.send('能收到吗？')  # 发送消息给自己
my_friend = bot.friends().search('林', Sex=1, City='揭阳')[0:]  # 搜索名称含有 "林" 的男性揭阳好友
# my_friend.send("祝大家元宵节快乐!")
# my_friend.send_image('元宵节.jpg')

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径
bot.enable_puid('wxpy_puid.pkl')
# 指定一个好友
my_friends = bot.friends().search('林')[0]  # [0]表示第一个
# 查看他的 puid
print(my_friends.puid)

all_Chat_object = bot.chats(bot.friends(update=True) + bot.groups(update=True) + bot.mps(update=True))  # 获取所有聊天对象
print(all_Chat_object)

if bot.friends(update=True):  # 获取所有好友
    # all_friends = bot.core.get_friends(update=bot.friends(update=True))
    # print(all_friends)
    Friend_all = bot.friends()  # 获取好友列表
    print(Friend_all.stats_text())  # 获取好友的统计信息
    Friends = bot.core.get_friends(update=True)[0:]  # 获取好友列表
    print(Friends)
    male = female = other = 0  # 初始化计数器，有男有女，当然，有些人是不填的
    for i in Friends[1:]:  # 遍历这个列表，列表里第一位是自己，所以从"自己"之后（也就是第二位）开始计算
        sex = i['Sex']
        if sex == 1:  # 1表示男性，2女性
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    total = len(Friends[1:])  # 计算好友总数
    # 输出男女比例
    print('男性：%.2f%%' % (float(male) / total * 100))
    print('女性：%.2f%%' % (float(female) / total * 100))
    print('未填性别：%.2f%%' % (float(other) / total * 100))
else:
    all_friends = bot._retrieve_itchat_storage('memberList')  # 获取所有好友
    print(all_friends)
labels = '男性', '女性', '未填性别'
sizes = [male, female, other]
explode = (0, 0.1, 0)
# 指定饼图某些部分的突出显示，即呈现爆炸式
# 其中第一个参数是‘男性’部分，0表示饼图合在一起，1表示分裂开来
# 其中第一个参数是‘女性’部分，0表示饼图合在一起，1表示分裂开来,0.1表示偏离的距离
# 其中第一个参数是‘未填性别’部分，0表示饼图合在一起，1表示分裂开来
fig1, ax1 = plt.subplots()  # 创建一个图形和一个子图
ax1.pie(sizes, explode=explode, labels=labels, autopct='%.2f%%', shadow=True, startangle=90)
# autopct：设置百分比格式，如'%.2f%%'为保留两位小数
# shadow：是否添加饼图的阴影效果
# startangle：设置饼图的初始摆放角度, 180为水平；
ax1.axis('equal')  # 相等的长宽比可确保将饼图绘制为圆形
plt.savefig('wechat_sex.png')  # 保存图片
bot.file_helper.send_image('wechat_sex.png')   # 向文件传输助手发送图片
bot.file_helper.send(str('男性：%.0f 位' % male))
bot.file_helper.send(str('女性：%.0f 位' % female))
bot.file_helper.send(str('未填性别：%.0f 位' % other))
thismanager = plt.get_current_fig_manager()
thismanager.window.wm_iconbitmap('LOGO.ico')
thismanager.canvas.set_window_title('林旭东的可视化图表')
plt.show()

if bot.mps(update=True):  # 获取所有公众号
    all_mps = bot.core.get_mps(update=bot.mps(update=True))
    print(all_mps)
else:
    all_mps = bot._retrieve_itchat_storage('mpList')
    print(all_mps)


@bot.register(my_friend)  # 回复 my_friend 的消息 (优先匹配后注册的函数!)
def reply_my_friend(msg):
    return 'received:{}({})'.format(msg.text, msg.type)


@bot.register(msg_types=bot.friends)
def auto_accept_friends(msg):  # 自动接受新的好友请求
    new_friend = msg.card.accept()  # 接受好友请求
    new_friend.send('您好！我自动接受了你的好友请求。')  # 向新的好友发送消息


embed()  # 进入 Python 命令行、让程序保持运行
# bot.join()  # 或者仅仅堵塞线程
