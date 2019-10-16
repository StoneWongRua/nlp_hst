# 导入数据分析包
import pandas as pd
import numpy as np

# 导入csv数据
# dtype = str,最好读取的时候都以字符串的形式读入，不然可能会使数据失真
# 比如一个0010008的编号可能会读取成10008

fileNameStr = r'C:\Users\15845\ch3_data.csv'
DataDF = pd.read_csv ( fileNameStr, encoding="ISO-8859-1", dtype=str )

# encoding = "ISO-8859-1" -- 用什么解码，一般会默认系统的编码，如果是中文就用 "utf-8"
DataDF = pd.read_csv ( fileNameStr, encoding="ISO-8859-1", dtype=str )


# # 用默认值填充:df.fillna(' ')
# DataDF.CustomerID= DataDF.CustomerID.fillna('Not Given')
#
# print(DataDF.loc[488696])
#
# # 用平均值填充:df.fillna(df.mean())
# DataDF.UnitPrice = DataDF.UnitPrice.fillna(DataDF.UnitPrice.mean())
# # 使用中位数填充
# DataDF.UnitPrice = DataDF.UnitPrice.fillna(DataDF.UnitPrice.median())
# # 使用众数填充
# DataDF.UnitPrice = DataDF.UnitPrice.fillna(DataDF.UnitPrice.mode().values)
#
# # 用相邻的值进行填充
# print(DataDF)
# print(DataDF.UnitPrice.fillna(method='ffill')) # 前向后填充
# print(DataDF.UnitPrice.fillna(method='bfill')) # 后向前填充

#字符串转换为数值（整型）
DataDF['Quantity'] = DataDF['Quantity'].astype('int')
#字符串转换为数值（浮点型）
DataDF['UnitPrice'] = DataDF['UnitPrice'].astype('float')

#定义函数：分割销售日期，获取销售日期
#输入：timeColSer 销售时间这一列，是个Series数据类型
#输出：分割后的时间，返回也是个Series数据类型
def SplitTime(timeColSer):
    timeList=[]
    for value in timeColSer:
        #例如2018-01-01 星期五，分割后为：2018-01-01
        dateStr=value.split(' ')[0]
        timeList.append(dateStr)
#将列表转行为一维数据Series类型
    timeSer=pd.Series(timeList)
    return timeSer

#数据类型转换:字符串转换为日期
#errors='coerce' 如果原始数据不符合日期的格式，转换后的值为空值NaT
print("日期格式调整前：")
print(DataDF.loc[:,'InvoiceDate'])
time = DataDF.loc[:,'InvoiceDate']
data_new = SplitTime(time)
DataDF.loc[:,'InvoiceDate'] = data_new
data_new=pd.to_datetime(DataDF.loc[:,'InvoiceDate'],
                                           format='%d/%m/%Y',
                                           errors='coerce')


# 查看数据集的信息
print("日期格式调整后：")
print(DataDF.loc[:,'InvoiceDate'])

#删除异常值：通过条件判断筛选出数据
#查询条件
querySer=DataDF.loc[:,'UnitPrice']>0
print("查询结果：")
print(querySer)
#应用查询条件
print('删除异常值前：',DataDF.shape)
DataDF=DataDF.loc[querySer,:]
print('删除异常值后：',DataDF.shape)