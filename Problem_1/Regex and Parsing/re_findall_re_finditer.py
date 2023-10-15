# Enter your code here. Read input from STDIN. Print output to STDOUT


import re

pattern = r'(?<=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])([aeiouAEIOU]{2,})(?=[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM])'


s = input()

m = list(map(lambda x: x.group(),re.finditer(pattern, s)))

if m:
    for x in m:
        print(x)
else:
    print(-1)
