# -*- coding: utf-8 -*-

import threading
import time


def createTimer():
    t = threading.Timer(2, repeat)
    t.start()


def repeat():
    print('Now:', time.strftime('%H:%M:%S', time.localtime()))
    createTimer()


createTimer()