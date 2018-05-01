# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import random
import string

list = string.ascii_uppercase

# 权重，升序排列
weighted = range(1, 27)

b = []
a = []
for idx, tmp in enumerate(list):
    for i, w in enumerate(weighted):
        if idx == i:
            a += [tmp] * w
            print(a)


def get_count(b):
    result = {}
    for tmp in b:
        num = b.count(tmp)
        if num > 1:
            result[tmp] = num - 1
    return result

def remove(li, di):
    result = li[:]
    for key, value in di.items():
        for tmp in range(value):
            result.remove(key)
    return result

def remove_src(li, di):
    result = li[:]
    for key in di:
        num = result.count(key)
        for i in range(num):
            # print(key, result)
            result.remove(key)
    return result

for i in range(50):
    b = random.sample(a, 10)
    tmp = get_count(b)
    r = remove(b, tmp)
    s = remove_src(a, r)
    print(b, tmp, r, s)
