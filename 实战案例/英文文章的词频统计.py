# --coding:utf-8--
import re
from collections import Counter

with open('doc', 'r') as txt:
    words = txt.read()

c3 = Counter(re.split('\\W+', words))
# print(c3.most_common(10))


l1 = [1, 2, 2, 3, 4, 5, 5, 6]
l2 = [(1, 2), (2, 3), (2, 3), (2, 1), (33, 1)]

c4 = Counter(l2)
print(c4.most_common(3), end='\n')
