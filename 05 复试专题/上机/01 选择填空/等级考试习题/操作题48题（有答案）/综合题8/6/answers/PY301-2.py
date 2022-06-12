# 请在...处使用多行代码替换
#
# 注意：其他已给出代码仅作为提示，可以修改

import jieba
f=open("data.txt","r")
lines=f.readlines()
f.close()

d = {}
for line in lines:
    wordList=jieba.lcut(line) #用结巴分词，对每行内容进行分词
    for word in wordList:
        if len(word)<3:
            continue
        else:
            d[word]=d.get(word,0)+1
ls=list(d.items())
ls.sort(key=lambda x:x[1],reverse=True)#按照词频由高到低排序
            
f=open('out2.txt','w')
for i in range(len(ls)):
    f.write('{}:{}\n'.format(ls[i][0],ls[i][1]))
f.close()




