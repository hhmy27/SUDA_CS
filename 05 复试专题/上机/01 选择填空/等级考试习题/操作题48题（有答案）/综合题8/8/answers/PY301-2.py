# 请在______处使用一行或多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

n = 0
m=0
f = open("univ.txt", "r")
lines=f.readlines()
f.close()
for line in lines:
    if '大学生' in line:
        continue
    elif '大学' in line:
        print('{}'.format(line))
        n+=1
    elif '学院' in line:
        print('{}'.format(line))
        m+=1
    

print("包含大学的名称数量是{}".format(n))
print("包含学院的名称数量是{}".format(m))
