# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("vote.txt")
names = f.readlines()
f.close()
D = {}
for name in names:
    if len(name.split())==1:
        D[name[:-1]]=D.get(name[:-1],0) + 1
l = list(D.items())
l.sort(key=lambda s:s[1],reverse=True)
name = l[0][0]
score = l[0][1]
print("最具人气明星为:{},票数为：{}".format(name,score))
