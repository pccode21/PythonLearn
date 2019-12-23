import say                #使用import语句导入say.py文件
say.say_hello()           #调用say.py文件中的say_hello()函数
from say import say_name  #从say.py中导入say_name()函数
say_name("林先生")         # 调用say_name()函数
import say as s           #指定say模块的别名为s
s.say_hello()             #使用s别名调用say模块中的函数
from say import *         #导入say模块中的所有函数
say.say_hello()           #调用say_hello()方法
say.say_name("林先生")     # 调用say_name()方法