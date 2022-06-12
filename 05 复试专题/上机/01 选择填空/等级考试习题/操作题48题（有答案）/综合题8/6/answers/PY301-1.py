# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba
f = open('data.txt','r')
lines=f.readlines()
f.close()
D=[]
for line in lines:
    wordList=jieba.lcut(line)#用结巴分词，对每行内容进行分词
    for word in wordList:
        if len(word)<3: #判断词长度，要大于等于3个长度
            continue
        else:
            if word not in D:
                D.append(word)
f=open('out1.txt','w')
f.writelines('\n'.join(D))            
f.close()
