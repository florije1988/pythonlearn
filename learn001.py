# -*- coding: utf-8 -*-
__author__ = 'florije'

pic_str = 'http://www.baidu.com/fuboqing.jpg,http://www.baidu.com/xiaoqigui.jpg'
print pic_str.split(',')
for item in pic_str.split(','):
    parts = item.split('/')
    if len(parts):
        file_name = parts.pop()
        file_path = '%s%s' % ('/'.join(parts), '/')
        print file_name
        print file_path

