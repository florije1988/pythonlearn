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
    '''
    This is the Student class
    '''
    def __init__(self, name, age):
        '''
        this is the init func in class Student
        :param name:
        :param age:
        :return:
        '''
        super(Student, self).__init__(name)
        self.age = age

    def show(self):
        '''
        This is the show func in class Student
        :return:nothing
        '''
        print 'self.name: %s, self.age: %s' % (self.name, self.age)

    def operation(self, a, b):
        '''

        :param a:
        :param b:
        :return:
        '''
        return a + b


if __name__ == '__main__':
    student = Student('florije', 15)
    print student.__doc__
    student.show()
    student.operation(1, 2)
