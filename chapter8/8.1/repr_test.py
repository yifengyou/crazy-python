# coding:utf-8
# File Name：     repr_test
# Author :        yifengyou
# Date :        2021/07/18
class Apple:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def __repr__(self):
        return "Apple[color=" + self.color + ",weight=" + str(self.weight)


a = Apple("红色", 5.68)
print(a)
