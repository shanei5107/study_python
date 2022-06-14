# -*- coding: utf-8 -*-

import time

ticks = time.time()
print('当前时间戳为:', ticks)

localtime = time.localtime(time.time())
print('本地时间为:', localtime)

import calendar
cal = calendar.month(2016, 1)
print(cal)