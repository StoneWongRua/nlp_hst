#导入数据分析包
import pandas as pd
import numpy as np

#导入csv数据
#dtype = str,最好读取的时候都以字符串的形式读入，不然可能会使数据失真
#比如一个0010008的编号可能会读取成10008

fileNameStr = r'C:\Users\15845\ch3_data.csv'
DataDF = pd.read_csv(fileNameStr,encoding = "ISO-8859-1",dtype = str)

# encoding = "ISO-8859-1" -- 用什么解码，一般会默认系统的编码，如果是中文就用 "utf-8"
DataDF = pd.read_csv(fileNameStr,encoding = "ISO-8859-1",dtype = str)

# 查看数据集的信息
DataDF.info()

# 查看每一列的数据类型
print(DataDF.dtypes)

# 有多少行，多少列
print(DataDF.shape)

# 检查缺失数据
# 如果你要检查每列缺失数据的数量，使用下列代码是最快的方法。
# 可以让你更好地了解哪些列缺失的数据更多，从而确定怎么进行下一步的数据清洗和分析操作。
print(DataDF.isnull()) # 查看是否是缺失值
print(DataDF.isnull().any()  )# 判断哪些"列"存在缺失值
print(DataDF[DataDF.isnull().values==True])  # 只显示存在缺失值的行列
print(DataDF.isnull().sum().sort_values(ascending=False)) # 输出每个列丢失值也即值为NaN的数据和，并从多到少排序

# 默认（axis＝0）是逢空值剔除整行，设置关键字参数axis＝1表示逢空值去掉整列
DataDF= DataDF.drop(['CustomerID'], axis = 1)

# 'any'如果一行（或一列）里任何一个数据有任何出现Nan就去掉整行，‘all’一行（或列）每一个数据都是Nan才去掉这整行
DataDF.dropna(how='any')
DataDF.dropna(how='all')

# 去掉这个特征为空的行
DataDF_new = DataDF.drop(DataDF[DataDF.UnitPrice.isnull()].index)
# 返回已经去掉重复行的数据集
DataDF.drop_duplicates()

# 更精细的thresh参数，它表示留下此行（或列）时，要求有多少［非缺失值］
DataDF.dropna(thresh = 6 )

# 查看数据集的信息
DataDF.info()

