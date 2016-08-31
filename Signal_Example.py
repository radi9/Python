#!/usr/bin/python
'''
30秒內沒收到'kill -USR1 PID',就結束程式
每收到'kill -USR1 PID', time就更新為30
'''
import signal
import time
import os
import sys

class Signal_Object:
  time = 30
  def __init__(self):
    signal.signal(signal.SIGUSR1, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.time = 20

if __name__ == '__main__':
  x = Signal_Object()
  print 'My PID is:', os.getpid()

  while x.time > 0:
    time.sleep(5)
    x.time = x.time - 1
    print"time : ",x.time

  print "End of the program"
