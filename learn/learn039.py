# -*- coding: utf-8 -*-
__author__ = 'florije'

if __name__ == '__main__':
    pass
    # 1, 2, 3, 4, 5, 6,
    solution = []
    origin = range(1, 7)
    for i1 in origin:
        for i2 in [item for item in origin if item != i1]:
            for i3 in [item for item in origin if item != i1 and item != i2]:
                for i4 in [item for item in origin if item != i1 and item != i2 and item != i3]:
                    for i5 in [item for item in origin if item != i1 and item != i2 and item != i3 and item != i4]:
                        for i6 in [item for item in origin if
                                   item != i1 and item != i2 and item != i3 and item != i4 and item != i5]:
                            if i1 + i2 + i3 == i3 + i4 + i5 == i5 + i6 + i1:
                                solution.append((i1, i2, i3, i4, i5, i6))
    print len(solution)




