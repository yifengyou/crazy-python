# coding:utf-8
# File Name：     Personal
# Author :        yifengyou
# Date :        2021/07/18
class Person:
    hair = 'black'

    def __init__(self, name='microease', age=24):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


p = Person()
print(p.name, p.age)
p.name = '李刚'
p.say("python语言很简单")
print(p.name,p.age)