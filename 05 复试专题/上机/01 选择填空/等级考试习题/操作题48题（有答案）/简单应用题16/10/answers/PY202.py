# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

names=input("请输入各个同学行业名称，行业名称之间用空格间隔（回车结束输入）：")
t=names.split()
d = {}
for c in range(len(t)):
    d[t[c]]=d.get(t[c],0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 按照数量排序
for k in range(len(ls)):
    zy,num=ls[k]
    print("{}:{}".format(zy,num))

