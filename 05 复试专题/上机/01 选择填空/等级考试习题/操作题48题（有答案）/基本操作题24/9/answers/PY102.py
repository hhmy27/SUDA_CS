# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

a = [3,6,9]
b =  eval(input()) #例如：[1,2,3]
s=0
for i in range(3):
    s += a[i]*b[i]
print(s)
