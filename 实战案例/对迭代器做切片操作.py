#! --coding:utf-8--
'''
读取文件某范围 如100 - 300行，并可以对行做迭代。

常见方法：
     f = open('file','r')
     list1 = f.readlines()
     list12 = list1[100:300]

    不足：readlines会一次性读取，导致内存不足

迭代器方法：
    使用 itertools 下的 islice 方法
    *islice会消耗迭代器，所有每次使用时，需要重新申请迭代器对象
'''

from itertools import islice

l = list(range(20))
print(l)
t = iter(l)

for i in islice(t, 2, 5):
    print(i, end=' ')
print()

for i in t:
    print(i, end=' ')
print()

#t = iter(l)

for i in t:
    print(i, end=' ')
