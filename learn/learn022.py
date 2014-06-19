# -*- coding: utf-8 -*-
__author__ = 'florije'


class A(object):
    def foo(self):
        print('class A')


class B(object):
    def foo(self):
        print('class B')


class C(A, B):
    pass


if __name__ == '__main__':
    c = C()
    c.foo()