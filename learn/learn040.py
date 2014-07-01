# -*- coding: utf-8 -*-
__author__ = 'florije'


class MyTest:
    myname = 'peter'

    def sayhello(hello):
        print "say hello to %s" % hello.myname


class UseWith(object):
    # def __init__(self):
    # self.text = 'UseWith'
    #     print '__init__'

    def __enter__(self):
        self.text = 'xiaoqi'
        print '__enter__'

    def show_txt(self):
        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'


class Context(object):
    def __init__(self, obj):
        self.obj = obj
        print '__init__()'

    def show(self):
        return self.obj

    def __enter__(self):
        print '__enter__'
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__'


if __name__ == '__main__':
    my = MyTest()
    my.sayhello()

    x, _ = (1, 2)
    print x
    print _

    # with UseWith() as test_with:
    #     test_with.show_txt()
        # u = UseWith()
        # u.show_txt()
    with Context([1, 2]) as context:
        print context.show()