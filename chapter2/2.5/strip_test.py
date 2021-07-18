# coding:utf-8
# File Name：     strip_test
# Author :        yifengyou
# Date :        2021/07/18
s = " this is a puppy "
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.strip())
print(s)
print(s.lstrip(" this"))
print("=========")
print(s.startswith(" "))
print(s.find("puppy"))
print(s.replace("puppy", "dog"))
print("=========")
print(s.split())
print(s.split("i"))
print("-".join(s.split()))