# -*- coding:utf-8 -*-
# @Author   :   Shawn
# @Time     :   2019/9/23 16:29
# @File     :   字符串对齐功能.py
# @Software :   PyCharm

"""
    实现打印字符串的左，中，右对齐功能

    方法1：使用字符串  str.ljust() str.rjust() str.center() 进行左中右对齐
    方法2：使用format（）方法，传递类似'<20','>20','^20'参数进行对齐

Disass    : 53.0
aaas      : 2
about     : 100.2
thanks    : 22
alloflove : 1024

"""

dic1 = {
    'Disass': 53.0,
    'aaas': 2,
    'about': 100.2,
    'thanks': 22,
    'alloflove': 1024
}

w = max(map(len, dic1.keys()))

for i in dic1:
    print(i.ljust(w), ':', dic1[i])