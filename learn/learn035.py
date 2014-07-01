# -*- coding: utf-8 -*-
__author__ = 'florije'

d = {"a": [1, 1], "c": [3, 3], "b": [2, 2]}

# a c b
# 1 3 2
# 1 3 2

keys = d.keys()
values = []
for key in d.keys():
    values.append(d[key])
print keys
print [item for item in zip(*values)]
