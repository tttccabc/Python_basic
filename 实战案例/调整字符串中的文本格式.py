#! -*-coding:utf-8-*-
"""
   把log文件中的日期从中文格式调整成英文格式。
   方法:使用正则表达式的匹配组方法sub(源re，目标re，对象）
"""

with open('log', 'r', encoding='utf-8') as log:
    str = log.read()
import re

# 使用匹配组，默认方式\1表示第一组
res = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\2-\1-\3', str)
print(res)

# 使用匹配组，命名方式
res1 = re.sub(r'(?P<g1>\d{4})/(?P<g2>\d{2})/(?P<g3>\d{2})', r'\g<g3>#\g<g1>#\g<g2>', str)
print(res1)
