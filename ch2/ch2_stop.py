from collections import Counter
import jieba

# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip () for line in open ( filepath, 'r' , encoding='UTF-8').readlines ()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut ( sentence.strip () )
    stopwords = stopwordslist ( r"C:\Users\15845\nlp_hst\ch2\res\stopword.txt" )  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr


inputs = open ( r"C:\Users\15845\nlp_hst\ch2\res\ai.txt", 'r' , encoding='UTF-8')  # 加载要处理的文件的路径
outputs = open ( r"C:\Users\15845\nlp_hst\ch2\res\ai_after.txt", 'w' , encoding='UTF-8')  # 加载处理后的文件路径

for line in inputs:
    line_seg = seg_sentence ( line )  # 这里的返回值是字符串
    outputs.write ( line_seg )
outputs.close ()
inputs.close ()
# WordCount
with open ( r"C:\Users\15845\nlp_hst\ch2\res\ai_after.txt", 'r' , encoding='UTF-8') as fr:  # 读入已经去除停用词的文件
    data = jieba.cut ( fr.read () )
data = dict ( Counter ( data ) )

with open ( r"C:\Users\15845\nlp_hst\ch2\res\ai_count.txt", 'w' , encoding='UTF-8') as fw:  # 读入存储wordcount的文件路径
    for k, v in data.items ():
        fw.write ( '%s,%d\n' % (k, v) )