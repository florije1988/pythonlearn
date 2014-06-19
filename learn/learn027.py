# -*- coding: utf-8 -*-
__author__ = 'florije'
from copy import copy, deepcopy

if __name__ == '__main__':
    list1 = [1, 2]
    list2 = list1
    list3 = list1[:]
    list4 = copy(list1)
    # 这里list2是添加了一个引用，list3和list4是一个浅拷贝，也就是把元素简单的拷贝走，然后单独的开一个
    print('list1:%s, list2:%s, list3:%s, list4:%s' % (id(list1), id(list2), id(list3), id(list4)))
    list2[0] = 3
    list3[0] = 4
    list4[1] = 5
    print list1
    print list2
    print list3
    print list4
    # result
    # [3, 2]
    # [3, 2]
    # [4, 2]
    # [1, 5]

    # 接下来看一下深拷贝的内容
    list1 = [[1], [2]]
    list2 = copy(list1)
    list3 = deepcopy(list1)
    print('list1:%s, list2:%s, list3:%s' % (id(list1), id(list2), id(list3)))
    list2[0][0] = 3
    print('list1:', list1)
    list3[0][0] = 5
    print('list1:', list1)
    print('list3:', list3)
