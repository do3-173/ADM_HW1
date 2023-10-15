# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

x = int(input())
shoe_sizes = Counter(list(map(int,input().split())))
n = int(input())

money_earned = 0
for i in range(n):
    customer = list(map(int,input().split()))
    if shoe_sizes[customer[0]] != 0:
        shoe_sizes[customer[0]] -= 1
        money_earned += customer[1]
print(money_earned)


