'''
Created on 2015年3月17日

@author: zhangzhizhi
'''
import time
import thread
def print_time(threadName,delay):
    count = 0
    while count < 10:
        time.sleep(delay)
        count += 1
        print(threadName)
        
