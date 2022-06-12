# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

f=open("py301-sunsign.csv","r")
x=input("请输入星座中文名称（例如，双子座）")
ls = []
for line in f:
    ls.append(line.strip('\n').split(','))
for row in ls:
    if row[1].count(x)>0:
      print("{}的生日位于{}-{}之间".format(x,row[2],row[3]))
f.close()


