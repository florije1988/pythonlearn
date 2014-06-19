# -*- coding: utf-8 -*-
__author__ = 'florije'


class MyClass(object):
    __private_variable = 10
    def public_method(self):
        print('This is the public_method.')

    def __private_method(self):
        print('This is the private_method.')

    def call_private_method_in_class(self):
        self.__private_method()

if __name__ == '__main__':
    myclass = MyClass()
    myclass.public_method()
    myclass.call_private_method_in_class()
    myclass._MyClass__private_method()
    print myclass._MyClass__private_variable