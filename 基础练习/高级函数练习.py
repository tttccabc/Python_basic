# -*- coding:utf-8 -*-
# @Author   :   Shawn
# @Time     :   2019/10/4 16:15
# @File     :   高级函数联系.py
# @Software :   PyCharm

f1 = lambda s: {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
snum = '245.678'
num1, num2 = snum.split('.')

print(list(map(f1, num1 + num2)))

