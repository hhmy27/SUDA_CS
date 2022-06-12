# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("vote.txt")
names = f.readlines()
f.close()
n = 0
for name in names:
    num = len(name.split())
    if num==1:
        n+=1
print("有效票{}张".format(n))
