# -*- coding: utf-8 -*-
__author__ = 'florije'
import json


class People(object):
    def __init__(self, name):
        self.name = name

if __name__ == '__main__':
    resp = dict()
    people = People('xiaoqibao')
    resp['return_code'] = {'people': people}
    result = json.dumps(resp)
    print result


    '''
    Traceback (most recent call last):
      File "D:/fuboqing/projects/python/pythonlearn/learn/learn014.py", line 14, in <module>
        result = json.dumps(resp)
      File "C:\Python27\lib\json\__init__.py", line 243, in dumps
        return _default_encoder.encode(obj)
      File "C:\Python27\lib\json\encoder.py", line 207, in encode
        chunks = self.iterencode(o, _one_shot=True)
      File "C:\Python27\lib\json\encoder.py", line 270, in iterencode
        return _iterencode(o, 0)
      File "C:\Python27\lib\json\encoder.py", line 184, in default
        raise TypeError(repr(o) + " is not JSON serializable")
    TypeError: <__main__.People object at 0x022E07F0> is not JSON serializable
    '''