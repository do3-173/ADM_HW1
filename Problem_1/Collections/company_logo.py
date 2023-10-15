#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    s = input()
    char_counter = Counter(sorted(s))
    for char, counter in char_counter.most_common(3):
        print(f"{char} {counter}")
        
