# -*- coding: utf-8 -*-
__author__ = 'florije'
import dis

if __name__ == '__main__':
    code_str = '''print "Hello, world"'''
    code_obj = compile(code_str, '<string>', 'exec')
    dis.dis(code_obj)