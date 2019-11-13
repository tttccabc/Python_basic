# --coding:utf-8--
'''
把某个字符串依据分隔符拆分成不同的字段，该字符串包含多种不同的分隔符，例如：
s='ab;cd|efg|hi,jk|mn\topq;rs,wud\tdfe'
其中<,><;><|><\t>都是分隔符，如何处理？
'''

# 单一分隔符
s1 = 'root      8550  0.0  0.1 1813092 27688 ?       Ssl  Jan29 157:46 /opt/naas/sbin/naas'
s1.split()  # 默认是空白字符，只能传入一种分隔符

# 多分隔符，使用re.split方法

import re


def mulsplit(str, ms):
    res = str
    return [x for x in re.split(ms, res) if x]


s = 'ab;cd|efg|hi,jk|mn\topq;rs,wud\tdfe,,'
print([x for x in re.split(r'[,;\t|]',s) if x])
