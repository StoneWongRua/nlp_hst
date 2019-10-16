data = [
    {"handsome":"y", "temp":"n", "height":"short", "upward":"n", "class":"n" },
    {"handsome":"n", "temp":"y", "height":"short", "upward":"y", "class":"n"},
    {"handsome":"y", "temp":"y", "height":"short", "upward":"y", "class":"y" },
    {"handsome":"n", "temp":"y", "height":"high", "upward":"y", "class":"y" },
    {"handsome":"y", "temp":"n", "height":"short", "upward":"y", "class":"n" },
    {"handsome":"y", "temp":"n", "height":"short", "upward":"y", "class":"n"},
    {"handsome":"y", "temp":"y", "height":"high", "upward":"n", "class":"y" },
    {"handsome":"n", "temp":"y", "height":"mid", "upward":"y", "class":"y"},
    {"handsome":"y", "temp":"y", "height":"mid", "upward":"y", "class":"y"},
    {"handsome":"n", "temp":"n", "height":"high", "upward":"y", "class":"y"},
    {"handsome":"y", "temp":"y", "height":"short", "upward":"n", "class":"n"},
    {"handsome":"y", "temp":"y", "height":"short", "upward":"n", "class":"n" }]

import pandas as pd
pd.DataFrame(data)

# 计算嫁与否的概率
def P(data,cls_val,cls_name="class"):
    count = 0.0
    for e in data:
        if e[cls_name] == cls_val:
            count += 1
    return count/len(data)

PY, PN = P(data,"y"), P(data, "n")
print("嫁的概率为：", PY)
print("不嫁的概率为：", PN)

print(PY, PN)

# 定义函数计算条件概率
def PT(data,cls_val,attr_name,attr_val,cls_name="class"):
    count1 = 0.0
    count2 = 0.0
    for e in data:
        if e[cls_name] == cls_val:
            count1 += 1
            if e[attr_name] == attr_val:
                count2 += 1
    return count2/count1

print("不帅也嫁的概率为：",PT(data,"y", "handsome", "n"))
print("性格不好也嫁的概率为：",PT(data,"y", "temp", "n"))
print("长得不高也嫁的概率为：",PT(data,"y", "height", "short"))
print("没上进心也嫁的概率为：",PT(data,"y", "upward", "n"))


# 计算单个属性的概率
def P_Attr(data,cls_val,cls_name):
    count = 0.0
    for e in data:
        if e[cls_name] == cls_val:
            count += 1
    return count/len(data)

print("不帅的概率为：",P_Attr(data, "n", "handsome"))
print("性格不好的概率为：",P_Attr(data,"n", "temp"))
print("长得不高的概率为：",P_Attr(data,"short", "height"))
print("没上进心的概率为：",P_Attr(data,"n", "upward"))



