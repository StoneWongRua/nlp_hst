import nltk

# 安装nltk相关套件
nltk.download()

# 加载book数据
from nltk.book import *



len(set(str))
len(str)/len(set(str))

str.count("秦")
str.count("大秦")
str.count("国")

fdist=FreqDist(str)
fdist.plot()

print(sorted (set(str[:100])))

fdist.plot(100,cumulative=True)



# 呈現中文
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.rcParams['font.sans-serif'] = 'SimHei'

with open(r"C:\Users\15845\nlp_hst\ch1\res\dqdg.txt","r+") as f: # 以读写模式[r+]打开文件dqdg.txt
    str=f.read()

tokens = nltk.word_tokenize(str)   # 标记化
mytext = nltk.Text(tokens)         # 将文本转换为NLTK Text对象
mytext.dispersion_plot(["秦","国","商鞅","王"])

from nltk import bigrams
from collections import Counter
b = bigrams('This is a test')
print(Counter(b))