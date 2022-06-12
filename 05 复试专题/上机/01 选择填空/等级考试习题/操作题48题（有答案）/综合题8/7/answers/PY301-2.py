'''
输入文件 ： candidate0.txt
输出文件 ： candidate.txt
'''
f=open("candidate0.txt",'r')
lines=f.readlines()
f.close()
D=[]
f=open('candidate.txt','w')
for line in lines:
    D=line.split()
    for i in range(10):
        if int (D[i+2])<0:
            break
    else:
        f.write('{}{}\n'.format(D[0],D[1]))
f.close()
