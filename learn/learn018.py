# -*- coding: utf-8 -*-
__author__ = 'florije'
from datetime import datetime
import json

json_dic = {'num': 1112, 'date': datetime.now()}

# print json.dumps(json_dic)  # TypeError: datetime.datetime(2014, 6, 17, 10, 58, 48, 600000) is not JSON serializable


class User(object):
    def __init__(self, name):
        self.name = name


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.__str__()
        if isinstance(obj, User):
            return obj.name
        return json.JSONEncoder.default(self, obj)


print json.dumps(json_dic, cls=DateEncoder)

json_2 = {'user': User('orangle')}

print json.dumps(json_2, cls=DateEncoder)