# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

f=open("data.txt","r")
lines=f.readlines()
f.close()

f = open("univ.txt", "w")
for line in lines:
    if 'alt' in line:  #判断是否有alt,若有则用'alt'分割，分割后再用'"'分割
        dx=line.split('alt=')[-1].split('"')[1]
        f.write('{}\n'.format(dx))
f.close()
