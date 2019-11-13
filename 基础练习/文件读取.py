# import sys
#
# for f in (sys.stdin, sys.stdout, sys.stderr):
#     print(f)
# file = open('temp.txt', 'w')
# with open('temp.txt', 'a') as file:
# 自动关闭打开文件的方式之一，依赖上下文管理器，比较简练


# try:
# file.write('hello world to file! \n')
# file.write('Bye   \n')
# file.writelines(['line one ', 'line two'])
# file.writelines(['line one \n', 'line two'])
# print(file.readline())

# open('temp', 'w').write("something")
# temp = open('temp', 'r').read()
# print(temp+' get ')
# finally:
#       file.close()
# 通用的显式文件关闭方式try/finally

#
# print(list(open('temp.txt')))
# lines = [line.rstrip() for line in open('temp.txt')]
# print(open('temp.txt').readlines())
# lines = [line.upper() for line in open('temp.txt')]
# print(lines)
#
# prin#t(list(map(str.split, open('temp.txt'))))
#
# line = 'hello world to file! \n'  #必须是一行，不能是一个字符串
# print(line in open('temp.txt'))
'''
file = open('temp.txt', 'r+')
print(file.tell())

file.write("99")
print(file.tell())
print(file.read())

file.seek(3)
file.write("00")
print(file.tell())
print(file.read())


sum = 0
start = 1
while start <=  100:
    sum += start
    start = start + 1

print(sum)



#print(open('temp.txt', 'w+').read())

#before = file.readline()
#print(before)

#file.write('rrr')
#print(file.readline())
#file.close()

#print(open('temp.txt').readlines())

#open mode
 #a 追加内容在文件尾部
 #r 读取文件，文件不存在则报错
 #w 写入文件默认会清空
 #a+ 打开文件并读写  1. 文件存在，打开文件，文件指针定位到文件开始位置，但不清空；
#                  2. 文件不存在，创建文件；
#                  3. 打开后读取时，在文件末尾位置，
#                  4. 写入时，添加到文章末尾，并且指针位于添加后的末尾，所以再次读取会乱码。
 #r+ 打开文件并读写  1. 文件存在，打开文件，文件指针定位到文件开始位置；
#                  2. 文件不存在， 则报错文件不存在
#                  3. 文件读取时，从开头读取
#                  4. 写入时未读取，覆盖写入开头；读取了，从末尾追加写入
 #w+ 打开文件并读写  1. 文件存在，则清空(也即写入空);
#                  2. 文件不存在，则创建文件 ;
#                  3. 文件流定位到开始位置， 所以read() 会得到空。

'''

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://s.taobao.com/search?q=球",timeout=30).text,"html.parser")
print(soup.prettify())
