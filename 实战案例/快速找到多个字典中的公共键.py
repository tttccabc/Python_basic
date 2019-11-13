# --coding:utf-8--
'''
 每轮进球的统计：
    第一轮： 梅西1  C罗2 苏亚雷斯3
    第二轮： 大罗2  梅西1
    第三轮： 格列兹曼2 C罗1
'''

from random import randint, sample
from functools import reduce

s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}

print(s1, "\n", s2, "\n", s3, "\n")

# 方法1： 使用迭代比较的方式
for i in s1:
    if i[0] in s2 and i[0] in s3:
        print(i[0], ":", s1[i[0]])

# 方法2： 使用set集合操作来实现
s4 = s1.keys() & s2.keys() & s3.keys()
print(s4)

map1 = map(dict.keys, [s1, s2, s3])
#print(map1)

s5 = reduce(lambda a, b: a & b, map1)
#print(s5)


for x in s4:
    print(x, s1[x] + s2[x] + s3[x])
