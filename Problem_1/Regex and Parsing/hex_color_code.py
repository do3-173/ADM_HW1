# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

pattern = r'#[0-9A-Fa-f]{3,6}'

css_lines = [input() for _ in range(n)]

inside_css = False
for line in css_lines:
    if '{' in line:
        inside_css = True
    elif '}' in line:
        inside_css = False
    elif inside_css:
        m = re.findall(pattern, line)
        for hex_color in m:
            print(hex_color)
