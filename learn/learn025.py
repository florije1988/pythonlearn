# -*- coding: utf-8 -*-
__author__ = 'florije'
import datetime

print('"datetime.time(0,0,0)" (Midnight) ->', bool(datetime.time(0, 0, 0)))
print('"datetime.time(0,0,0)" (Midnight) ->', bool(datetime.time(1, 0, 0)))