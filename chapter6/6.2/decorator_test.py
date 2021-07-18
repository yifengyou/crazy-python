# coding:utf-8
# File Name：     decorator_test
# Author :        yifengyou
# Date :        2021/07/18
def funA(fn):
    print("A")
    fn()
    return "hello"


@funA
def funB():
    print("B")


print(funB)
