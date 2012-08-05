#!/usr/bin/python

import os
import time

# get the status
stat = os.popen('vmstat')
# get time to create file with proper name
t = time.asctime().split()
# pop day and time
t.pop(0)
tm = t.pop(2)
f_name = ''
f_name = f_name.join(t)
# absolute address
f_name = '/home/sunny/vmstat/' + f_name

# open the file and append current status
f = open(f_name, 'a+')
f.write(tm + "\n")
f.write(stat.read())
f.write("\n")
f.close()


