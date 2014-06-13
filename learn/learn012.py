# -*- coding: utf-8 -*-
__author__ = 'florije'
import time


def timeit(func):
    start = time.clock()
    func()
    end = time.clock()
    print 'used:', end - start


def timeit2(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print 'used:', end - start

    return wrapper


def foo():
    print 'in the foo1'


@timeit2
def foo1():
    print 'in the foo1'


def foo2():
    start = time.clock()
    print 'in the foo2'
    end = time.clock()
    print 'used:', end - start


if __name__ == '__main__':
    foo1()
    timeit(foo)
