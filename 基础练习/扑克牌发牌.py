# --coding:utf-8--
import random
from random import randint

num = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
suit = ('club', 'heart', 'diamond', 'spade')

card = [(x, y) for x in num for y in suit]
cards = card * 2

# print(len(cards))
# print(cards.pop(randint(0, len(cards))))
# print(len(cards))

player1 = []
player2 = []
player3 = []
player4 = []

for i in range(26):
    player1.append(cards.pop(randint(0, len(cards)-1)))
    player2.append(cards.pop(randint(0, len(cards)-1)))
    player3.append(cards.pop(randint(0, len(cards)-1)))
    player4.append(cards.pop(randint(0, len(cards)-1)))
    print("  {0} ".format(i))

print(player1)
print(player2)
print(player3)
print(player4)

player1.sort(key=lambda x: x[1])
player2.sort(key=lambda x: x[1])
player3.sort(key=lambda x: x[1])
player4.sort(key=lambda x: x[1])

print()
print(player1)
print(player2)
print(player3)
print(player4)