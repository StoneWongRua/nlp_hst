import io
import os
import sys
import logging

import jieba

import Word2vec
from gensim.models import word2vec



file_name = r'C:\Users\15845\nlp_hst\Word2vec\data'
train_file_name = file_name + 't_cut'
model_file = file_name + '.model'
model_file_bin = file_name + '.model.bin'

# 此函数作用是对初始语料进行分词处理后，作为训练模型的语料
def cut_txt(old_file, cut_file):
    print ("begin")
    try:
        # read file context
        fi = io.open(old_file, 'r', encoding='utf-8')
        text = fi.read()  # 获取文本内容

        # cut word
        new_text = jieba.cut(text, cut_all=False)  # 精确模式
        str_out = ' '.join(new_text).replace('，', '').replace('。', '').replace('？', '').replace('！', '') \
        .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
        .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
        .replace('’', '')     # 去掉标点符号

        # write to cut_file
        fo = io.open(cut_file, 'w', encoding='utf-8')
        fo.write(str_out)
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息
    print  ("end")

def model_train(train_file_name, save_model_file):  # model_file_name为训练语料的路径,save_model为保存模型名
    print("begin")
    try:
        # 模型训练，生成词向量
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        sentences = word2vec.Text8Corpus(train_file_name)  # 加载语料
        model = word2vec.Word2Vec(sentences, size=200)  # 训练skip-gram模型; 默认window=5
        model.save(save_model_file)
        model.wv.save_word2vec_format(save_model_file + ".bin", binary=True)   # 以二进制类型保存模型以便重用
    except BaseException as e:  # 因BaseException是所有错误的基类，用它可以获得所有错误类型
        print(Exception, ":", e)    # 追踪错误详细信息
    print("end")



def word2vec_test():
    print ('word2vec_test begin.')
    try:
        # 加载日志输出配置
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

        # 加载文件切词
        print ('加载文件:%s 切词后存放为:%s.' % (file_name, train_file_name))
        if not os.path.exists(file_name):    # 判断文件是否存在，参考：https://www.cnblogs.com/jhao/p/7243043.html
            print ('加载文件切词失败。')
            exit(0)
        else:
            cut_txt(file_name, train_file_name)  # 须注意文件必须先另存为utf-8编码格式

        # 训练模型
        print( '从文件:%s 训练模型存放在: %s' % (train_file_name, model_file))
        if not os.path.exists(model_file):     # 判断文件是否存在
            model_train(train_file_name, model_file)
        else:
            print('此训练模型已经存在，不用再次训练')

        # 加载已训练好的模型
        print ('从文件:%s 中加载模型' % model_file)
        # model_1 = gensim.models.KeyedVectors.load_word2vec_format(model_file_bin, binary=True)
        model_1 = word2vec.Word2Vec.load(model_file)

        # 计算两个词的相似度/相关程度
        y1 = model_1.similarity(u"赵敏", u"韦一笑")
        print ( u"赵敏和韦一笑的相似度为: %g" % y1)
        y2 = model_1.similarity ( u"赵敏", u"赵敏" )
        print ( u"赵敏和赵敏的相似度为: %g" % y2 )
        y3 = model_1.similarity ( u"赵敏", u"周芷若" )
        print ( u"赵敏和周芷若的相似度为: %g" % y3 )
        print ("-------------------------------\n")

        # 计算某个词的相关词列表
        y2 = model_1.most_similar(u"张三丰", topn=20)  # 20个最相关的
        print(u"和张三丰最相关的词有:\n")
        for item in y2:
            print ("%s: %g" % (item[0], item[1]))
        print("-------------------------------\n")
    except Exception as e:
            print( "Exception", e)
    print ('word2vec_test end.')

if __name__ == "__main__":
    word2vec_test()



