# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

f = open("vote.txt")
names = f.readlines()
f.close()
n = 0
for name in _______(1)_________:
    num = _______(2)_________
    if _______(3)________:
        n+=__(4)____
print("有效票{}张".format(n))
