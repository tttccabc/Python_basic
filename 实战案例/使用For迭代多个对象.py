# ！--coding:utf-8--
'''
在for循环中使用for语句迭代多个可迭代对象

如:
  某班学生城市 语数外存储在3个列表中，同时迭代三个列表（并行）

  某年纪4个班，某次考试每班成绩存储在4个列表中，依次迭代每个列表，统计全年级高于90分人数（串行）

'''
from random import randint
from itertools import chain

l1 = [randint(60, 100) for _ in range(40)]
l2 = [randint(60, 100) for _ in range(40)]
l3 = [randint(60, 100) for _ in range(40)]
# 使用索引如
for i in range(len(l1)):
    print(l1[i] + l2[i] + l3[i], end=' ')

# 通用方法   并行（zip） ，串行（itertools.chain）
# print(zip([1, 2, 3, 4], ('a', 'b', 'c', 'd'),[3,3,3]))
print()
sum = []
for x, y, z in zip(l1, l2, l3):
    sum.append(x + y + z)
print(sum)

print()
big = []
for i in chain(l1, l2, l3):
    if i > 90:
        big.append(i)
print(len(big), big)
