import matplotlib.pyplot as plt
from wordcloud import WordCloud
from scipy.misc import imread

# 读入背景图
mask = imread(r"C:\Users\15845\nlp_hst\ch2\res\heart.png")

import jieba

# 读入要处理的文本
text_from_file_with_apath = open(r'C:\Users\15845\nlp_hst\ch2\res\sunny.txt').read()

# jieba分词
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

# 生成词云
my_wordcloud = WordCloud(font_path=r"C:\Users\15845\nlp_hst\ch2\res\simsun.ttf", # 兼容中文字体，不然中文会显示乱码
                         background_color="white",# 设置背景颜色
                         max_words=50,
                         mask = mask # 设置背景图
                         ).generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()