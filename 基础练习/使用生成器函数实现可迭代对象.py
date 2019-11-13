# --coding:utf-8--

'''
生成器对象  包含yield的函数，如下：
    def f():
    print("in f(),1")
    yield 1

    print("in f(),2")
    yield 2

    print("in f(),3")
    yield 3


    g = f()
    print(type(g))
    print(iter(g))
    print(g.__next__())

    <class 'generator'>
    <generator object f at 0x00AB3D30>
    in f(),1
    1


    实现一个函数，传递一个数值范围，打印出范围内的素数
    primeNum(start,end)

    for x in primeNum(1,100)
       print(x)

'''


class primeNum:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isPrimeNum(k):
                yield k


for i in primeNum(1, 100):
    print(i)
