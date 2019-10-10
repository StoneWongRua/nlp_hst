import nltk

# 安装nltk相关套件
nltk.download()

# 加载book数据
from nltk.book import *

# 关键字检索
text3.concordance("lived")

# 找到用法、意义与该单词相似的词
text1.similar("monstrous")

# 找到用法、意义与该单词集合相似的词
text1.common_contexts(["monstrous","abundant"])

# 相异字词
set(text4)

# 相异字词排序
sorted(set(text4))

# 定义词汇多样性的函数
def lexical_diversity(text):
    return len(set(text)) / len(text) # 相异字词长度/总字词长度

print(lexical_diversity(text4))

# 构造文本的词汇分布图
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America", "liberty", "constitution"])

# 普通频率查找：
fdist1=FreqDist(text1) # 查询文本text1中词汇分布情况
fdist1.plot(50,cumulative=True) # 输出指定常用词累积频率图

# hapaxes()函数 返回低频词
print(fdist1.hapaxes())
print(len(fdist1.hapaxes()))

# 细粒度查找
V = set ( text1 )
longwords=[w for w in V if len(w) > 15]
sorted(longwords)