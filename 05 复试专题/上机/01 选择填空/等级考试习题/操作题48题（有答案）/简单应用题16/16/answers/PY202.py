#请完善如下代码
#在....处填写多行代码，不得修改其他代码
#PY202.py


while True:
    s = input("请输入不带数字的文本:")
    i=0
    for p in s:
        if "0"<=p<="9":
            i=i+1
    if i==0:
        break
print(len(s))
