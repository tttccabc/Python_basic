# -*- coding:utf-8 -*-
# @Author   :   Shawn
# @Time     :   2019/11/12 20:22
# @File     :   派生内置不可变类型并修改实例化行为.py
# @Software :   PyCharm

# 派生一个IntTuple类，继承tuple类，过滤元组中的非int对象，产生元组

class IntTuple(tuple):
    # def __new__(cls, iterable):
    #     n = (x for x in iterable if isinstance(x, int) and x > 0)
    #     return super(IntTuple, cls).__new__(cls, n)

    def __init__(self, iterable):
        super(IntTuple, self).__init__()


t = IntTuple([1, -1, 'abc', 5, ['x', 'y'], 3])
print(t)
