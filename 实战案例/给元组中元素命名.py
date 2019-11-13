# --coding:utf-8--
# 如何为元组中的每个元素命名，提高程序的可读性？
'''
    学生信息：（姓名，年龄，性别，邮箱地址）
    ? 使用index索引访问，大量索引降低程序可读性，如何解决问题？

    C语言，通过 Define name 1 /  枚举类型

    ！元组优势: 占用空间小，速度快
'''

student1 = ('jim', 14, 'male', 'jim@com')

# print(student1[0])  # name
# print(student1[1])  # age
# 索引值不直观


# 解决方案1 通过常量定义
'''
# name = 0
# age = 1
# sex = 2
# email = 3
name, age, sex, email = range(4)

print(name, age, sex, email)
print(student1[name])
print(student1[age])
print(student1[sex])
'''

# 解决方案2 使用标准库中 namedtuple（命名元组）

from collections import namedtuple

stu = namedtuple('student', ['name', 'age', 'sex', 'email'])
s1 = stu('jim', 14, 'male', 'jim@com')
s2 = stu(age=13, name='rose', sex='female', email='Ramotic@tetannic.com')

print(s1)
print(s2)
print(s1.email, s2.email)

# isinstance(s1,tuple)  s1 是元组的子类，可以兼容使用