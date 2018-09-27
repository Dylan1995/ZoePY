#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# ------------------------------------------------------------------------------
data1 = "by Olivia 四月 30, 2018"
data2 = "by Lavender 四月 22, 2018"
data3 = "by Bear 五月 1, 2018"

"""
if "四月" in data1:
    data1.replace("四月", "4")
"""

for data in [data1, data2, data3]:
    d = re.findall(r"by\s(\w+)\s([\w\s,]+)", data)
    #print(d) # [("", ""),]
    author = d[0][0]
    date = d[0][1] # datetime.strptime("4 30, 2018", "%m %d, %Y")
    
    #print(author, ":", date)

    
# ------------------------------------------------------------------------------    
data = '''
哈囉你好
by Olivia 四月 30, 2018

ㄏㄏ好棒
by Lavender 四月 22, 2018

你好啊
by Bear 五月 1, 2018
'''
#[(), (), ()]
print(re.findall(r"by\s(\w+)\s([\w\s,]+?)\n", data))
for d in re.findall(r"by\s(\w+)\s([\w\s,]+?)\n", data):
    author = d[0]
    date = d[1]
    
    #print(author, ":", date)