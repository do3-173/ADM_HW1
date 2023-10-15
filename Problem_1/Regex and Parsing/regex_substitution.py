# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

pattern_and = r'(?<= )&&(?= )'
pattern_or = r'(?<= )\|\|(?= )'

for _ in range(n):
    s = input()
    print(re.sub(pattern_and, 'and', re.sub(pattern_or, 'or', s)))
        
        
