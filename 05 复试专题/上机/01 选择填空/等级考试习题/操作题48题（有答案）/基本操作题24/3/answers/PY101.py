# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

ntxt = input("请输入4个数字(空格分隔):")
nls=ntxt.split()
x0 = eval(nls[0])
y0 = eval(nls[1])
x1 = eval(nls[2])
y1 = eval(nls[3])
r = pow(pow(x1-x0, 2) + pow(y1-y0, 2), 0.5) 
print("{:.2f}".format(r))
