# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

data = input()  # 姓名 年龄 性别
s=0
n=0
i=0
while data:
    i=i+1
    ls=data.split()
    s=s+int(ls[2])
    if ls[1]=='男':
        n=n+1
    data = input()
s=s/i
print("平均年龄是{:.2f} 男性人数是{}".format(s,n))
