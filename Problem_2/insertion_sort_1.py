#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    for i in range(n-1, 0, -1):
        if i >= 0:  
            if arr[i] < arr[i-1]:
                temp = arr[i]
                j = i
                while temp < arr[j-1]:
                    arr[j] = arr[j-1]
                    print(" ".join(map(str, arr)))
                    j -= 1
                    if j == 0:
                        break
                arr[j] = temp
                print(" ".join(map(str, arr)))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
