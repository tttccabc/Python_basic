# -- coding:utf-8 --
'''
  1. 随机序列中找到出现次数最高的3个元素，以及出现次数。
  2. 对某英文文章做词频统计，找出出现次数最高的10个词和次数。
'''

from random import randint

data = [randint(0, 20) for _ in range(30)]
print(data)

result = dict.fromkeys(data, 0)
print(result)

for x in data:
    result[x] += 1

# print(result)

# 方法1 使用zip把字典转换成元组，在用list构造成list
# 使用sorted函数排序list，使用reverse逆序（降序）
tuple_temp = list(zip(result.values(), result.keys()))
tuple_temp1 = list(zip(result.keys().__iter__(), result.values().__iter__()))
print("\n\n\n",tuple_temp1,"\n\n")
tuple_temp = sorted(tuple_temp, reverse=True)
# 打印前三
# for i in range(3)
#    print(tuple_temp[i])


# 方法2 使用sorted的函数的key参数。
dict_temp = sorted(result.items(), key=lambda x: x[1], reverse=True)
for i in range(3):
    print("项目是：{name}，值是：{val}".format(name=dict_temp[i][0], val=dict_temp[i][1]), end='   ')
# print(dict_temp)


from collections import Counter

c2 = Counter(result)
print(c2)
