# -*- coding: utf-8 -*-
__author__ = 'florije'
if __name__ == '__main__':
    print [item for elem in zip([1, 2, 3], ['a', 'b', 'c']) for item in elem]

    tuple_list = zip([1, 2, 3], ['a', 'b', 'c'])
    for elem in tuple_list:
        for item in elem:
            print item
    zip_data = zip([1, 2, 3], [4, 5, 6])
    print zip_data
    res_list = ()

    for item in zip_data:
        res_list = res_list + item

    print res_list
    # reduce(lambda x, y: x + y, zip(a, b))
    print reduce(lambda x, y: x + y, zip_data)

    print zip([1, 2, 3], [4, 5, 6])
    print map(list, zip([1, 2, 3], [4, 5, 6]))
    print sum([[1, 4], [2, 5], [3, 6]], [])
    print sum(map(list, zip([1, 2, 3], [4, 5, 6])), [])

    print sum([1, 2, 3], 4)