# 导入wordcloud模块和matplotlib模块
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取一个txt文件
text = open(r'C:\Users\15845\nlp_hst\ch2\res\english.txt','r').read()

# 生成词云
wordcloud = WordCloud(background_color='white',scale=1.5).generate(text)

# 显示词云图片
plt.imshow(wordcloud)
plt.axis('off')
plt.show()
