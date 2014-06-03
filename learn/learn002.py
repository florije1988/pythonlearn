# -*- coding: utf-8 -*-
__author__ = 'florije'


def foo(positional_arg, keyword_arg='default', *tuple_arg, **dict_arg):
    print "positional arg: ", positional_arg
    print "keyword_arg: ", keyword_arg
    print type(tuple_arg)
    print tuple_arg
    for each_additional_arg in tuple_arg:
        print "additional_arg: ", each_additional_arg
    print type(dict_arg)
    print dict_arg
    for each_dict_arg in dict_arg.keys():
        print "dict_arg: %s=>%s" % (each_dict_arg, str(dict_arg[each_dict_arg]))


# def dict_to_param(kwargs):
#     mark_args = []
#     for key in kwargs.keys():
#         if kwargs[key] is None:
#             pass
#         else:
#             mark_args.append("%s='%s'" % (key, kwargs[key]))
#     return mark_args


if __name__ == '__main__':
    # foo(1)
    # foo(1, '2')
    # foo(1, '2', 3)
    # foo(1, '2', 3, a='4')
    regular_param = 1
    default_param = '2'
    tuple_params = (3,)
    dict_params = {'a': '4'}

    foo(regular_param, default_param, *tuple_params, **dict_params)  # you must know this is a param to get the dict_parm

