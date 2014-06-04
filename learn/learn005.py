# -*- coding: utf-8 -*-
__author__ = 'florije'

# apply() filter()

# apply( func[, nkw[, kw]] )
# 该函数的目的是将非关键字参数和关键字参数传入到func函数中调用，其中nkw是非关键字参数，kw是关键字参数，返回值是函数调用的返回值。
# 然而，由于目前的Python中，已经可以在函数调用中使用非关键字参数和关键字参数作为可变长参数调用,
# apply()已经被从Python1.6开始被摒弃淘汰.因此，此处仅对该函数进行一个大致的介绍，而不具体深入，也不应在编程中再使用该函数。

# filter( func, seq )
# 该内建函数的作用相当于一个筛子。func函数是一个布尔函数，filter()调用这个布尔函数，将每个seq中的元素依次过一遍筛子，
# 选出使func返回值是Ture的元素的序列。

if __name__ == '__main__':
    scores = [55, 80, 83, 64, 91, 100, 90, 79]

    def score_filter(score):
        return 80 <= score < 90
    # regular method
    filtered_score = []
    for each in scores:
        if score_filter(each):
            filtered_score.append(each)

    print(filtered_score)

    print filter(score_filter, scores)

    print [score for score in scores if 80 <= score < 90]