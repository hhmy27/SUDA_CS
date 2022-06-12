#请完善如下代码,不得修改其他代码
#在________处填写一行或多行代码
#PY102.py

n = input()
s = "〇一二三四五六七八九"
for c in "0123456789":
     n=n.replace(c,s[int(c):int(c)+1])
print(n)
