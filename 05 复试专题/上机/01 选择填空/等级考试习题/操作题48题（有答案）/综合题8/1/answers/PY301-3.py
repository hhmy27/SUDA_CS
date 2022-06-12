# 以下代码为提示框架
# 请在...处使用一行或多行代码替换
#
# 注意：提示框架代码可以任意修改，以完成程序功能为准

txt=open("命运.txt","r").read()
for ch in ' \n':
    txt=txt.replace(ch,"")
d = {}
for ch in txt:
    d[ch]=d.get(ch,0)+1
ls = list(d.items())
ls.sort(key=lambda x:x[1], reverse=True) # 此行可以按照词频由高到低排序
string=""
for i in range(len(ls)):
    s=str(ls[i]).strip("()")
    string=string+s[1]+':'+s[5:]+','
f=open("命运-频次排序.txt","w")
f.write(string)
f.close()
