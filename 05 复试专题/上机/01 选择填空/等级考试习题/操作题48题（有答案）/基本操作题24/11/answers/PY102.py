# 请在______处使用一行代码或表达式替换
#
# 注意：请不要修改其他已给出代码

import jieba
txt = input("请输入一段中文文本:")
ls=jieba.lcut(txt)
print("{:.1f}".format(len(txt)/len(ls)))
