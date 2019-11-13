# --coding:utf-8--
from random import randint
import os
from collections import deque
import pickle

# res = randint(1, 100)
# print(type(res))  # 值为int类型
#
# his = deque([], 5)
# gue = input("Let me guess a number or check history.")
# while True:
#     his.append(int(gue))
#     if res > int(gue):
#         print("lower than result. ")
#     elif res < int(gue):
#         print("higher than result. ")
#     elif res == 'h':
#         print(list(his))
#     gue = input("Let me guess a number or check history.")
#
# print("sucessfully! ")


res = randint(1, 100)
#print(res)
if os.path.exists("his"):
    his = pickle.load(open("his", 'rb'))
else:
    his = deque([], 5)

#print(type(his))

gue = input("Let me guess a number.")
while True:
    if gue.isdigit():
        his.append(gue)
        if res > int(gue):
            print("lower than result. ")
        elif res < int(gue):
            print("higher than result. ")
        else:
            break
    elif gue == 'h':
        print(list(his))
    elif gue == 'exit':
        pickle.dump(his, open("his", 'wb'))
        exit("exit.")
    else:
        print('\033[1;31m')
        print("Usage: h view history.")
        print('\033[0m')

    gue = input("Let me guess a number.")

print("Sucessfully! ")
