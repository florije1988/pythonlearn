# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    test_str = '5404A6AF10DD'
    list_str = test_str[::2]
    print list_str
    print [test_str[e:e + 2] for e in range(0, 11, 2)]
    print "-".join(['5404A6AF10DD'[item:item + 2] for item in range(0, len('5404A6AF10DD') - 1, 2)])
