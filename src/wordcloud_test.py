from wordcloud import WordCloud
import jieba
import numpy as np
import PIL.Image as Image
def chinese_jieba(text):
    wordlist_jieba=jieba.cut(text)
    space_wordlist=' '.join(wordlist_jieba)
    return space_wordlist
text=open('/eclipse-workspace/txt/python.txt').read()
text=chinese_jieba(text)
# 调用包PIL中的open方法，读取图片文件，通过numpy中的array方法生成数组
mask_pic=np.array(Image.open('/eclipse-workspace/pictures/python.png'))
wordcloud = WordCloud(font_path='C:/Windows/Fonts/simfang.ttf',#设置字体
                      mask=mask_pic,#设置背景图片
                      background_color="white",#设置背景颜色
                      max_font_size=150,# 设置字体最大值
                      max_words=2000, # 设置最大显示的字数
                      stopwords={'Python'}, #设置停用词，停用词则不再词云图中表示
                      ).generate(text)
image=wordcloud.to_image()
wordcloud.to_file('/eclipse-workspace/pictures/python_wordcloud.png')
image.show()