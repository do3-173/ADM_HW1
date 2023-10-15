#!/bin/python3

import math
import os
import random
import re
import sys

import calendar
def timestamp_to_seconds(t1):
    _, day, month, year, time, timezone = t1.split()
    hh, mm, ss = map(int, time.split(':'))
    
    months = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
        'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    month_num = months[month]
    
    timezone_offset = int(timezone[0] + timezone[1:3]) * 3600 + int(timezone[0] + timezone[3:5]) * 60
    
    return calendar.timegm((int(year), month_num, int(day), hh, mm, ss)) - timezone_offset


# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(abs(timestamp_to_seconds(t1) - timestamp_to_seconds(t2)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
