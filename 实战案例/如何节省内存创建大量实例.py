# -*- coding:utf-8 -*-
# @Author   :   Shawn
# @Time     :   2019/11/12 20:43
# @File     :   如何节省内存创建大量实例.py
# @Software :   PyCharm

# 类似游戏实例，有上百万个用户，如何降低这些大量实例的内存开销
# 解决方案：定义里的__slots__属性，用来声明实例属性名字的列表
import sys


class player1():
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class player2():
    __slots__ = ['uid', 'name', 'stat', 'level']
    # slots方法静态定义了类的属性（没有__dict__方法），因此这个类不能动态绑定属性，从而减小了内存占用

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


p1 = player1('001', 'p1')
p2 = player2('002', 'p2')

p1.new = 'new'
# del p1.new # 注销一个属性值
# 动态绑定一个新属性

print(dir(p1))
print(dir(p2))
# 显示p1,p2的属性集合

print(dir(p1.__dict__))

# 显示p1,p2的属性集合


print(set(dir(p1)) - set(dir(p2)))
# 通过集合的差集，看看p1比p2多了什么？

print(sys.getsizeof(p1.__dict__))
# 看看p1多的属性占用的内存空间大小
