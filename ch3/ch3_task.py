# 导入numpy、pandas包
import datetime

import numpy as np
import pandas as pd

# 导入数据
salesDf = pd.read_excel(r'C:\Users\15845\Share_180210\朝阳医院2018年销售数据.xlsx',dtype='object')

#当excel中只有一个数据工作表时，用下面的函数直接读取数据也可以。
#salesDf = pd.read_excel(r'D:\dataFile\朝阳医院2018年销售数据.xlsx', dtype='object')

# 查看导入数据的基本状况

# 查看导入数据的类型
print("数据的类型: ")
print(type(salesDf))

# 查看导入数据的每个项目的类型
print("项目的类型： ")
print(salesDf.dtypes)

# 查看数据的基本大小
print("数据的基本大小: ")
print(salesDf.shape)

# 查看开头几行数据，看看数据是否读取正确
print("前五行数据为：")
print(salesDf.head())

# 用描述函数describ来查看一下整个数据的基本状况
print("数据的基本描述：")
print(salesDf.describe())


# 购药时间->销售时间
nameChangeDict = {'购药时间':'销售时间'}
# 参数inplace=True表示覆盖元数据集
salesDf.rename(columns = nameChangeDict,inplace=True)

# 查看开头几行数据，看看数据是否修改正确
print("前五行数据为：")
print(salesDf.head())

# 查看一下哪些项目存在缺失值
print(salesDf.isnull().any())

# 查看一下缺失值的数量
# 通常可以用isnull函数来查找缺失值
print(salesDf[salesDf[['销售时间','社保卡号']].isnull().values == True])

# 去掉重复数据
naDf = salesDf[salesDf[['销售时间','社保卡号']].isnull().values == True].drop_duplicates()
print(naDf)

print("删除前数据集规模显示:")
print(salesDf.shape)


#含有销售时间和社保卡号的缺失数据删除
salesDf = salesDf.dropna(subset=['销售时间','社保卡号'],how = 'any')
print("删除后数据集规模显示:")
print(salesDf.shape)

# 重命名行名（index）：排序后的列索引值是之前的行号，需要修改成从0到N按顺序的索引值
salesDf=salesDf.reset_index(drop=True)

salesDf['销售数量'] = salesDf['销售数量'].astype('float')
salesDf['应收金额'] = salesDf['应收金额'].astype('float')
salesDf['实收金额'] = salesDf['实收金额'].astype('float')
print('转换后的数据类型：')
print(salesDf.dtypes)


# 日期转换
def dateChange(dateSer):
    dateList = []
    for i in dateSer:
        #例如2018-01-01 星期五，分割后为：2018-01-01
        str = i.split(' ')[0]
        dateList.append(str)
    dateChangeSer = pd.Series(dateList)
    return dateChangeSer

dateChangeSer = dateChange(salesDf['销售时间'])
print(dateChangeSer)

print(salesDf['销售时间'].isnull().any())
print(salesDf.dtypes)



#按销售时间排序
salesDf = salesDf.sort_values(by='销售时间')
#再次更新一下序号
salesDf = salesDf.reset_index(drop = True)

print(salesDf.head())

#删除异常值：通过条件判断筛选出数据
#查询条件
querySer=salesDf.loc[:,'销售数量']>0
# 应用查询条件
print('删除异常值前：',salesDf.shape)
salesDf=salesDf.loc[querySer,:]
print('删除异常值后：',salesDf.shape)


# 把销售时间的数据类型转换为日期型
dateOut=pd.to_datetime(salesDf['销售时间'], format = '%Y-%m-%d', errors='coerce')

# 总消费次数计算
kpDf = salesDf.drop_duplicates(subset=['销售时间','社保卡号'])
total = kpDf.shape[0]
print('总消费次数为：',total)



# 月份数计算

def parse(time_str):
    """
    Parse time format.
    :param time_str: <str> time string
    :return: <datetime.date> date
    """
    time_list = time_str.split ( "-" )
    year = time_list[0]
    month = time_list[1]
    day = time_list[2]

    return datetime.date ( int ( year ), int ( month ), int ( day ) )

startDay = salesDf.loc[0,'销售时间'].split(' ')[0] # 最小时间值
dateChangeOut = dateChange(salesDf['销售时间'])
print('开始日期:',parse(startDay))
endDay = salesDf.loc[salesDf.shape[0]-1,'销售时间'].split(' ')[0]  #最大时间值
print('结束日期:',parse(endDay))
monthCount = (parse(endDay) - parse(startDay)).days #函数.days计算天数，“//”表示取整数
print('月份数:',monthCount)


# 月均消费次数 = 总消费次数 / 月份数
kpi1 = total / monthCount
print('业务指标1：月均消费次数=',kpi1)

# 月均消费金额 = 总消费金额 / 月份数
totalMoney = salesDf['实收金额'].sum()
kpi2 = totalMoney / monthCount
print('月平均消费金额=',kpi2)