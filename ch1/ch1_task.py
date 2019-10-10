import nltk
from nltk.book import *

# 以读写模式[r+]打开文件dqdg.txt
with open(r"C:\Users\15845\nlp_hst\ch1\res\dqdg.txt","r+") as f:
    str=f.read()


# 查看大秦帝国第一部总共有多大的用字量，即不重复词和符合的尺寸：
print(len(set(str)))
print(len(str)/len(set(str)))

# 查看常用词
str.count("秦")
str.count("大秦")
str.count("国")

# 中文
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.rcParams['font.sans-serif'] = 'SimHei'

# 词汇离散分布查看
tokens = nltk.word_tokenize(str)   # 标记化
mytext = nltk.Text(tokens)         # 将文本转换为NLTK Text对象
mytext.dispersion_plot(["秦","国","商鞅","王"])

# 查看累积分布：
fdist=FreqDist(str)
fdist.plot()

# 高频分析
sorted(set(str[:1000]))

# 低频分析
FreqDist(str).hapaxes()

