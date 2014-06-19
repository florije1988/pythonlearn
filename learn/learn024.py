# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    a_list = []
    print 'id:%s' % id(a_list)
    a_list += [4]
    print('id(+=):%s' % id(a_list))
    a_list = a_list + [5]
    print('id(a=a+...):%s' % id(a_list))

    a_list = []
    print 'id:%s' % id(a_list)
    a_list.append(1)
    print('id(append):%s' % id(a_list))
    a_list.extend([2])
    print('id(extend):%s' % id(a_list))
