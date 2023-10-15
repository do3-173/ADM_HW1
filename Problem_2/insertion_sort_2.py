#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    for k in range(1, n):
        for i in range(k, 0, -1):
            if i >= 0:  
                if arr[i] < arr[i-1]:
                    temp = arr[i]
                    j = i
                    while temp < arr[j-1]:
                        arr[j] = arr[j-1]
                        j -= 1
                        if j == 0:
                            break
                    arr[j] = temp
                    
        print(" ".join(map(str, arr)))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
