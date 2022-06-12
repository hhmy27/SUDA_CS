# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f=open("earpa001.txt","r")
fo=open("earpa001_count.txt","w")
d = {}
for line in f:
    t=line.strip(' \n').split(',')
    s=t[2]+'-'+t[3]
    d[s]=d.get(s,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=False) # 该语句用于排序
for i in range(len(ls)):
    a,b=ls[i]
    fo.write('{},{}\n'.format(a,b))
f.close()
fo.close()
