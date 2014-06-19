# -*- coding: utf-8 -*-
__author__ = 'florije'
import dis

if __name__ == '__main__':
    tup = ([],)
    # tup[0] += [1]
    tup[0].extend([1])
    print tup
    dis.dis(compile('x[0] += [1]', '<string>', 'exec'))

    my_tup = (1,)
    print id(my_tup)
    my_tup += (4,)
    print id(my_tup)
    my_tup = my_tup + (5,)
    print my_tup
    print id(my_tup)


