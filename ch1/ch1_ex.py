# -*- coding=utf-8 -*-

# 词语搭配和双连词
from nltk import bigrams
from collections import Counter

b = bigrams('This is a test')
print(Counter(b))
