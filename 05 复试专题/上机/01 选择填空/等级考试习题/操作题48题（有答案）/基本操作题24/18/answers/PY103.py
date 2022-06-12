# 请在...处使用一行或多行代码替换
#
# 注意：请不要修改其他已给出代码

n = eval(input("请输入数量："))
if n>0 and n<=1:
    cost=n*160
elif n<=4:
    cost=n*160*0.9
elif n<=9:
    cost=n*160*0.8
else:
    cost=n*160*0.7
cost=int(cost)
print("总额为:",cost)
