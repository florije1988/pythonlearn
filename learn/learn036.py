# -*- coding: utf-8 -*-
__author__ = 'florije'


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


def func(a, b, c=0, *args, **kwargs):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kwargs


def fib(i, current = 0, next = 1):
    if i == 0:
        return current
    else:
        return fib(i - 1, next, current + next)


def f():
    return f()


if __name__ == '__main__':
    nums = [1, 2, 3]
    print calc(*nums)

    args = (1, 2, 3, 4)
    kw = {'x': 99}
    func(*args, **kw)

