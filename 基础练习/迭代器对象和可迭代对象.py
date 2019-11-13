# --coding:utf-8--
'''
iter(l) 实际调用了  l的__iter__()方法。
对于字符串，s.__getitem()方法。

for循环，是调用对象的 next(),直到异常跳出。

iter?
Docstring:
iter(iterable) -> iterator
iter(callable, sentinel) -> iterator
Get an iterator from an object.  In the first form, the argument must
supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel.
Type:      builtin_function_or_method
'''

import requests
from _collections_abc import Iterable, Iterator


# print(getWeather(u'北京'))
# print(getWeather(u'北京'))


class WeatherIterator(Iterator):
    def __init__(self, cities):  # 城市名称列表
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s , %s ' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


for x in WeatherIterable([u'马鞍山', u'廊坊', u'合肥', u'无为', u'上海', u'南京']):
    print(x)
