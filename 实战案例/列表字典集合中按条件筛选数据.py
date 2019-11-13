from random import randint

# 过滤列表中[3,1,2,4,-2,2]的负数
# 筛选出字典{'lilei':72, 'jim':22, 'lucy': 91} 中值高于90的项
# 筛选出集合中{22,44,5,55,66}中可以被3整除的元素

# ---通用方法 for循环迭代,使用if语句判断
# data = [-1, 2, 4, 3, -3, 6]
#
# res = []
# for i in data:
#     if i < 0:
#         res.append(i)
# print(res)

# ---高级方法
'''
    列表:
        列表解析: [x for x in data if x >= 0]
        filter函数: filter(lamda x: x >= 0, data)
    字典:
        字典解析:{k:v for k,v in d.items() if v > 90}
    集合:
        集合解析:{x for x in s if x%3 == 0}
'''

# ------------------列表实例--------------------
# l1 = [randint(-5, 20) for _ in range(10)]
# print(l1)
#
# res = [x for x in l1 if x > 0]
# print(res)
#
# g = filter(lambda x: x >= 0, l1)
# # filter 在2.7版本之前直接返回一个列表,在2.7之后返回一个迭代对象,可以使用g.next()查看值
#
# res_f = list(g) # 把迭代对象传给list构造器,产生list对象
# print(res_f)
#

# ------------------字典示例---------------------
# dict1 = {'student%d' % i: randint(50, 100) for i in range(1, 21)}
# print(dict1)
# res_dict = {k: v for k, v in dict1.items() if v >= 90}
# print(res_dict)
#
# g = filter(lambda item: item[1] >= 90, dict1.items())
# res_f = list(g)
# print(res_f)

# ------------------元组示例---------------------
t1 = {randint(10, 50) for x in range(20)}
print(t1)
res_tuple = {x for x in t1 if x % 3 == 0}
print(res_tuple)

res_f = list(filter(lambda x: x % 3 == 0, t1))
print(res_f)

