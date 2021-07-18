# coding:utf-8
# File Name：     locals_test
# Author :        yifengyou
# Date :        2021/07/18
def test():
    age = 20
    print(age)
    print(locals())
    print(locals()['age'])
    locals()['age']
    print('xxx',age)
    globals()['x'] = 19
x = 5
y = 20
test()
print(globals())
