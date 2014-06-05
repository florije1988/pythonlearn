# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    list_demo = [1, 2, 5, 3, 5]
    print list_demo.count(4)
    list_demo.append(4)
    print list_demo
    list_demo.extend([6, 7])
    print list_demo
    sorted_list = sorted(list_demo)
    print sorted_list, list_demo
    list_demo.sort()
    print list_demo
    print list_demo.pop(0)
    print list_demo
    list_demo.insert(0, 1)
    print list_demo
    list_demo.remove(1)  # maybe get the error of "ValueError: list.remove(x): x not in list"
    print(list_demo)

    print [1, 2, 3] + [5, 6, 9]

