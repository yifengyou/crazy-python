# coding:utf-8
# File Name：     function_test
# Author :        yifengyou
# Date :        2021/07/18
def my_max(x, y):
    z = x if x > y else y
    return z


def say_hi(name):
    print("正在执行say_hi函数")
    return name + "您好"


a = 6
b = 9
result = my_max(a,b)
print(result)
print(say_hi("胡炎凯"))
