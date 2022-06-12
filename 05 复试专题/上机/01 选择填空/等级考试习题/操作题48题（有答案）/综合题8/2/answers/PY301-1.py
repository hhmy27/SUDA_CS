# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
# 请在______处使用一行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

fi=open("sensor.txt","rb")
fo=open("earpa001.txt","wt")
for line in fi:
    ls=str(line,encoding="utf-8").strip(' \r\n').split(',')
    if ls[1].count("earpa001")>0:
        fo.write('{},{},{},{}\n'.format(ls[0],ls[1],ls[2],ls[3]))
fi.close()
fo.close()

