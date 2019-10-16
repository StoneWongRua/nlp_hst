import sys
import logging
from gensim.models import word2vec


train_file_name = r'C:\Users\15845\nlp_hst\Word2vec\datat_cut.txt'
save_model_file = r"C:\Users\15845\nlp_hst\Word2vec\倚天屠龙记.model"

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

if __name__ == "__main__":
    model_train(train_file_name, save_model_file)