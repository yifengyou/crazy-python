# coding:utf-8
# File Name：     for_list
# Author :        yifengyou
# Date :        2021/07/18
src_list = [12, 45, 3.4, 13, 'a', 4, 56, 'crazyit', 109]

my_sum = 0
my_count = 0

for ele in src_list:
    if isinstance(ele, int) or isinstance(ele, float):
        print(ele)
        my_sum += ele
        my_count += 1
print(my_count)
print(my_sum)
