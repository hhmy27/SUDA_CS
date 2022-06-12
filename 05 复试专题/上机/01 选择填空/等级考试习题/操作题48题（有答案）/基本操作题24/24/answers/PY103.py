#请完善如下代码,不得修改其他代码
#PY103.py

a, b, c = eval(input())
ls = []
for i in range(c):
    ls.append(str(a*(b**i)))
print(",".join(ls))

