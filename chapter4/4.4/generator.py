# coding:utf-8
# File Name：     generator
# Author :        yifengyou
# Date :        2021/07/18
c_generator = (x * x for x in range(10) if x % 2 == 0)
for i in c_generator:
    print(i,end="\t")
print()
