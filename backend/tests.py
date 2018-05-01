# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import random
import string
# Create your tests here.
# 选项
list = string.ascii_uppercase

# 权重，升序排列
weighted = range(1, 27)

def weighted_random(list, weighted, num):
    # 从1到权重之和间随机抽取一个整数
    r = random.randint(1, sum(weighted))

    print(r)
    # 把权重依此相加，直到大于或等于随机数r，相加的次数记为n，跳出循环
    # 从选项列表中取 n-1 位作为输出的加权随机数
    c = 0
    for index, w in enumerate(weighted):
        c = c + w
        if c >= r:
            return (list[index])
            break
all = []
for i in range(700):
    all.append(weighted_random(list, weighted, 8))
print('A:', all.count("A"))
print('B:', all.count("B"))
print('C:', all.count("C"))
