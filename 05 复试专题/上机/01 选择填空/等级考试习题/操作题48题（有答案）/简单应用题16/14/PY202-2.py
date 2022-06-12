# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("vote.txt")
names = f.readlines()
f.close()
D = {}
for name in _______(1)_________:
    if len(_____(2)______)==1:
        D[name[:-1]]=_______(3)_________ + 1
l = list(D.items())
l.sort(key=lambda s:s[1],_______(4)_________)
name = l[0][0]
score = l[0][1]
print("最具人气明星为:{},票数为：{}".format(name,score))
