# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
将对Python提供的调用可执行对象的内建函数进行说明，涉及exec、eval、compile三个函数。exec语句用来执行存储在代码对象、字符串、文件中的
Python语句，eval语句用来计算存储在代码对象或字符串中的有效的Python表达式，而compile语句则提供了字节编码的预编译。
当然，需要注意的是，使用exec和eval一定要注意安全性问题，尤其是网络环境中，可能给予他人执行非法语句的机会。
'''

if __name__ == '__main__':
    # exec obj
    exec 'print("fuboqing")'
    exec """for i in range(5):
                print(i)
        """
    # eval( obj[, globals=globals(), locals=locals()] )
    x = 7
    print eval('3 * x')

    # compile( str, file, type )
    '''
    compile语句是从type类型（包括’eval’: 配合eval使用，’single’: 配合单一语句的exec使用，’exec’: 配合多语句的exec使用）中将str
    里面的语句创建成代码对象。file是代码存放的地方，通常为”。compile语句的目的是提供一次性的字节码编译，就不用在以后的每次调用中重新
    进行编译了。还需要注意的是，这里的compile和正则表达式中使用的compile并不相同，尽管用途一样。
    '''

    eval_code = compile('1+2', '', 'eval')
    print eval(eval_code)
    single_code = compile('print "pythoner.com"', '', 'single')
    exec (single_code)

    exec_code = compile("""for i in range(5):
        print "iter time: %d" % i""", '', 'exec')

    exec(exec_code)



