'''

'''
f=open("name.txt")
names=f.readlines()
f.close()
f=open("vote.txt")
votes=f.readlines()
f.close()
f.close()
f=open("vote1.txt","w")
D={}
NUM=0
for vote in _______(1)________:
    num = len(vote.split())
    if num==1 and vote in _______(2)________:
        D[vote[:-1]]=_______(3)________+1
        NUM+=1
    else:
        f.write(_______(4)________)
f.close()        
l=list(D.items())
l.sort(key=lambda s:s[1],_______(5)________)
name=____(6)____
score=____(7)____
print("有效票数为：{} 当选村长村民为:{},票数为：{}".format(NUM,name,score))


