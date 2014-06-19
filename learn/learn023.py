# -*- coding: utf-8 -*-
__author__ = 'florije'


class A(object):
    def foo(self):
        print('class A')


class B(A):
    # def foo(self):
    #     print('class B')
    pass


class C(A):
    def foo(self):
        print('class C')


class D(B, C):
    pass

if __name__ == '__main__':
    print D.mro()
    print D.__mro__
    d = D()
    d.foo()