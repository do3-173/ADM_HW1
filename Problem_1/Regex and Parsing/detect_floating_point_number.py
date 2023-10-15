# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    s = input()
    pattern = r'^[+-.]?(\d*\.\d+)$'
    if re.match(pattern, s):
        print(True)
    else:
        print(False)
            
