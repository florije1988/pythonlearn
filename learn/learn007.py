# -*- coding: utf-8 -*-
__author__ = 'florije'


class User(object):
    '''
    This is a User model
    '''

    def __init__(self, name='name'):
        '''
        this function will init the class
        :param name:
        :return:
        '''
        print('This is in the __init__ func')
        self.name = name

    def __new__(cls, *args, **kwargs):
        '''
        this function will new the class
        :param cls:
        :param args:
        :param kwargs:
        :return:
        '''
        print('This is in the __new__ func')
        return super(User, cls).__new__(cls, *args)  # if no this line, won't call the init function

    def __str__(self):
        '''
        this function will return something new about this class
        :return:
        '''
        return 'Class User in __str__ func'

    def __repr__(self):
        '''
        This is will return the repr of this class
        :return:
        '''
        return "Class User in __repr__ func"

    def __del__(self):
        print('This is in the __del__ func')

if __name__ == '__main__':
    user = User('fuboqing')
    if user:
        print user.name
        print user
        print user.__repr__()

