# -*- coding: utf-8 -*-
__author__ = 'florije'


class SuperList(list):
    def __sub__(self, b):
        a = self[:]  # 这里，self是SuperList的对象。由于SuperList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a


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

    print SuperList([1, 2, 3]) - SuperList([3, 4])

