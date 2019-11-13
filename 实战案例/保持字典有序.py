# -- coding:utf-8 --
"""
    比赛记录选手成绩和用时 {'Jim':(2,33),'Rose':(1,23)}
    按排名顺序一次打印选手信息的实现。
"""

data = {}
data['Jim'] = (1, 35)
data['Kim'] = (2, 37)
data['Sim'] = (3, 39)

# for k in data: print(k)  # 这个迭代是不保证顺序的，随机的。

from collections import OrderedDict

# 通过OrderedDict字典，保持输出是的结果和加入字典顺序一致。

data1 = OrderedDict()

data1['Jim'] = (1, 35)
data1['Kim'] = (2, 37)
data1['Sim'] = (3, 39)

# for k in data: print(k)

from time import time
from random import randint

players = list('ABCDEFGH')
start = time()
course = OrderedDict()

for i in range(8):
    input()
    player = players.pop(randint(0, 7 - i))
    end = time()
    print(i + 1, player, end - start)
    course[player] = (i + 1, end - start)

print(course)
