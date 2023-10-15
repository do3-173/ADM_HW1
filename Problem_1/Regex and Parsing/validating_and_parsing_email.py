# Enter your code here. Read input from STDIN. Print output to STDOUT

import email.utils
import re

n = int(input())

pattern = r'^[a-zA-Z][\w\.-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

for _ in range(n):
    s = input()
    parse = email.utils.parseaddr(s)
    if re.match(pattern, parse[1]):
        print(s)
        
