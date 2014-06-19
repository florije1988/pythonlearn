# -*- coding: utf-8 -*-
__author__ = 'florije'


if __name__ == '__main__':
    a = 1
    b = 1
    c = 300
    d = 300
    print(a == b, a is b)
    print(c == d, c is d)  # 这种的在shell里面运行的时候就会发现是不对的。


    '''
    In [37]: a = 1

    In [38]: b = 1

    In [39]: print('a is b', bool(a is b))
    ('a is b', True)

    In [40]: c = 999

    In [41]: d = 999

    In [42]: print('c is d', bool(c is d))
    ('c is d', False) # 原因是python的内存管理,缓存了-5 - 256的对象

    In [43]: print('256 is 257-1', 256 is 257-1)
    ('256 is 257-1', True)

    In [44]: print('257 is 258-1', 257 is 258 - 1)
    ('257 is 258-1', False)

    In [45]: print('-5 is -6+1', -5 is -6+1)
    ('-5 is -6+1', True)

    In [46]: print('-7 is -6-1', -7 is -6-1)
    ('-7 is -6-1', False)
    In [47]: a = 'hello world!'

    In [48]: b = 'hello world!'

    In [49]: print('a is b,', a is b)
    ('a is b,', False) # 很明显 他们没有被缓存,这是2个字段串的对象

    In [50]: print('a == b,', a == b)
    ('a == b,', True) # 但他们的值相同
    # But, 有个特例
    In [51]: a = float('nan')

    In [52]: print('a is a,', a is a)
    ('a is a,', True)

    In [53]: print('a == a,', a == a)
    ('a == a,', False) # 亮瞎我眼睛了~
    '''
