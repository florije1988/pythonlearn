# -*- coding: utf-8 -*-
__author__ = 'florije'


class Person(object):
    '''
    This is the Person class
    '''
    def __init__(self, name):
        '''
        this is the init func
        :param name:
        :return: nothing
        '''
        self.name = name

    def show(self):
        '''
        This is the show func, will return the instance name
        :return:
        '''
        return self.name


class Student(Person):
    def __init__(self, name, age):
        super(Student, self).__init__(name)
        self.age = age

    def show(self):
        print 'self.name: %s, self.age: %s' % (self.name, self.age)


if __name__ == '__main__':
    student = Student('florije', 15)
    student.show()
