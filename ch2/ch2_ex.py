from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)
frequencies = {u'知乎': 0.1,  u'小段同学': 0.4,  u'曲小花': 0.3,  u'中文分词': 0.1,  u'样例': 0.1}
wordcloud = WordCloud(font_path="STSONG.TTF").fit_words(frequencies)

plt.imshow(wordcloud)
plt.axis("off")
plt.show()
