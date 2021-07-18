# coding:utf-8
# File Name：     for_expr
# Author :        yifengyou
# Date :        2021/07/18
a_range = range(10)
a_list = [x * x for x in a_range if x % 2 == 0]
print(a_list)
