# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

sort_s = ''.join(sorted(s, key=lambda x: (not x.islower(), not x.isupper(), x.isdigit(), x.isdigit() and  not int(x) % 2 == 1, x)))

print(sort_s)
