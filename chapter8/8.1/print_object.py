# coding:utf-8
# File Name：     print_object
# Author :        yifengyou
# Date :        2021/07/18
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


im = Item('鼠标', 19.8)
print(im)
print(im.__repr__())
