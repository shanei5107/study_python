# -*- coding: utf-8 -*-

import threading
import time

exitFlag = 0


class MyThread(threading.Thread):

    def __init__(self, threadId, name, delay):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.delay = delay

    def run(self):
        print('开始线程: ' + self.name)
        threadLock.acquire()
        print_time(self.name, self.delay, 5)
        threadLock.release()
        print('退出线程: ' + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print('%s: %s' % (threadName, time.ctime(time.time())))
        counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
    t.join()

# thread1.join()
# thread2.join()

print('退出主线程')