# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改


f=open("score.txt","r")
lines=f.readlines()
f.close()
D=[]  #单个学生的数据
L=[]  #L中的元素是学生原始成绩和总成绩
for line in lines:
    D=line.split()
    s=0  #每个学生的总成绩初始值
    for i in range(10):
        s+=int(D[i+2]) #各科成绩累加求和，+2是因为前两个元素是学号和姓名
    D.append(s)
    L.append(D)

L.sort(key=lambda x:x[-1],reverse=True)   #按学生总成绩从大到小排序
f=open('candidate0.txt','w')
for i in range(10):  #取前十个学生数据
    for j in range(len(L[i])): #一个学生的各项数据
        f.write('{} '.format(L[i][j])) #写各项数据，用空格隔开
    f.write('\n')  #换行
f.close()


    
