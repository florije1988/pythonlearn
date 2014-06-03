# -*- coding: utf-8 -*-
__author__ = 'florije'
# lambda [arg1[, arg2, ... argN]]: expression

if __name__ == '__main__':
    def true():
        return True

    true_lambda = lambda: True
    print true(), true_lambda()

    def add(x, y):
        return x + y
    add_lambda = lambda x, y: x + y
    print add(1, 2), add_lambda(1, 2)

    result = lambda x = 1, y = 2: x + y
    print result(), result(3, 4)

    c = lambda *z: z
    print c(10, 'test')
