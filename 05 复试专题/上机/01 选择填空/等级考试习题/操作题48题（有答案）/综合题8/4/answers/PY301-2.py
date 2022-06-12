# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f=open("py301-sunsign.csv","r")
x=input("请输入星座序号（例如，5）：")
ls = []
for line in f:
    ls.append(line.strip('\n').split(','))
num=x.split()
for i in num:
    for row in ls:
        if row[0]==i:
            if len(row[2])==3:
                m1=row[2][0]
                d1=row[2][1:3]
            else:
                m1=row[2][0:2]
                d1=row[2][2:4]
            if len(row[3])==3:
                m2=row[3][0]
                d2=row[3][1:3]
            else:
                m2=row[3][0:2]
                d2=row[3][2:4]
            print("{}({})的生日是{}月{}日至{}月{}日之间".format(row[1],row[4],m1,d1,m2,d2))
f.close()
