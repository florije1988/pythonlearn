# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
python 自省，也就是其他语言里面的反射
'''

import sys
import inspect
import types


def foo():
    pass


class Cat(object):
    '''
    This is the Cat class
    '''
    def __init__(self, name='kitty'):
        self.name = name

    def say_hi(self):
        print self.name


if __name__ == '__main__':
    cat = Cat()
    # print Cat.say_hi()
    print cat.say_hi()
    print dir(cat)
    print dir(Cat)
    if hasattr(cat, 'name'):
        setattr(cat, 'name', 'fuboqing')
    print getattr(cat, 'name', 'kitty')

    getattr(cat, 'say_hi')()
    print(len(dir(types)))

    import fnmatch as m
    print m.__doc__.splitlines()[0]
    print m.__name__
    print m.__file__
    print m.__dict__.items()[0]

    print Cat.__doc__
    print Cat.__name__
    print Cat.__module__
    print Cat.__bases__
    print Cat.__dict__

    print cat.__dict__
    print cat.__class__
    print cat.__class__ == Cat


