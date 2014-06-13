# -*- coding: utf-8 -*-
__author__ = 'florije'


def throw_error():
    raise Exception('raise a error!')


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal'
            else:
                raise

if __name__ == '__main__':
    # throw_error()
    mc = MuffledCalculator()
    mc.calc('1/0')