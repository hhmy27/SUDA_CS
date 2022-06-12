# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码
import random
random.seed(0)
s = 0
for i in range(5):
    n = random.randint(1,97)  # 产生随机数
    s = s+n**2
print(s)
