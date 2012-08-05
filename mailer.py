#!/usr/bin/python

import time
import os

# get current time to create get the correct file of the day
t = time.asctime().split()
# pop day and time
t.pop(0)
t.pop(2)
f_name = ''
f_name = f_name.join(t)
name = f_name
# absolute address of the file
f_name = '/home/sunny/vmstat/' +  f_name

# mail the file as an attachment
os.system("uuencode " + f_name + " report.txt | mail -s Report" + name + " example@example.com")

