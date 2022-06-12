# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语-原文.txt", "r")
fo = open("论语-提纯原文.txt", "w")
for line in fi:
    for k in range(100):#可以打开给定文件看一下最大值
        line=line.replace('('+str(k)+')','')
    fo.write(line)
fi.close()
fo.close()
