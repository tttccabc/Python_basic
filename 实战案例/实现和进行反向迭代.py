#! --coding:utf-8--

'''
*不改变对象和产生新对象的情况下进行反向迭代

*实现一个连续浮点数发生器FloatRange(),给定范围和步进值，产生一些连续浮点数：
   FloatRange(3.0,4.0,0.2)
   正向：3.0，3.2，3.4，3.6，3.8，4.0
   反向: 4.0,3.8,3.6,3.4,3.2,3.0
'''


# l = [x for x in range(10)]
# print(l)
# print(list(reversed(l)))  # 使用reversed函数实现逆向


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step


for x in FloatRange(1.0, 4.0, 0.4):
    print(x)

for x in reversed(FloatRange(1.0, 4.0, 0.4)):
    print(x)
