# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    a_list = [1, 2, 3]
    try:
        print('third element:', a_list[2])
    except IndexError:
        print('raised IndexError')
    else:
        print('no error in try-block')  # 只有在try里面没有异常的时候才会执行else里面的表达式

    i = 0
    while i < 2:
        print(i)
        i += 1
    else:
        print('in else')

    i = 0
    while i < 2:
        print(i)
        i += 1
        break
    else:
        print('completed while-loop')

    for i in range(2):
        print i
    else:
        print('completed range-loop')

    for i in range(2):
        print i
        break
    else:
        print('completed range-loop')
