# coding: utf-8
import io
import sys
import jieba

file_name = r'C:\Users\15845\nlp_hst\Word2vec\data'
cut_file = r'C:\Users\15845\nlp_hst\Word2vec\datat_cut.txt'


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


if __name__ == "__main__":
    cut_txt(file_name, cut_file)