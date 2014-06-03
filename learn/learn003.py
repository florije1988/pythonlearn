# -*- coding: utf-8 -*-
__author__ = 'florije'

# this is the program to test the func map and reduce

# map( func, seq1[, seq2...] )

if __name__ == '__main__':
    print range(6)
    print [x % 3 for x in range(6)]
    print map(lambda x: x % 3, range(6))

    a = [1, 2, 3]
    b = [4, 5, 6]
    zipped = zip(a, b)
    print zipped
    print zip(*zipped)

    print map(lambda x, y: x * y, [1, 2, 3], [4, 5, 6])
    print map(lambda x, y, z: (x * y + z, x + y - z), [1, 2, 3], [4, 5, 6], [1, 2, 3])  # [(4, 5), (10, 7), (18, 9)]

    print map(None, [1, 2, 3], [4, 5, 6])  # [(1, 4), (2, 5), (3, 6)]

    print zip([1, 2, 3], [4, 5, 6])  # [(1, 4), (2, 5), (3, 6)]

    # reduce( func, seq[, init] )
    n = 5
    print reduce(lambda x, y: x * y, range(1, n + 1))  # 120
    m = 2
    n = 5
    print reduce(lambda x, y: x * y, range(1, n + 1), m)

