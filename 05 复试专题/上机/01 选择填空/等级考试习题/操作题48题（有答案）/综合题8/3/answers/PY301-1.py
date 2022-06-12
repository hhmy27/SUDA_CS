# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准


fi = open("论语.txt", "r")
fo = open("论语-原文.txt", "w")
a=0
for line in fi:
    if a==1 and line.count("【注释】")==0 and line.count("【原文】")==0:
        line = line.strip(" \n")
        if line.strip():#判断line是否为空串
            fo.write('{}\n'.format(line))
    if line.count("【原文】")>0:
        a=1
    if line.count("【注释】")>0:
        a=0
fi.close()
fo.close()
