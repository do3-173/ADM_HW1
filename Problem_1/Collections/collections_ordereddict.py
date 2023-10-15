# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

n = int(input())
items_prices = OrderedDict()
for _ in range(n):
    item = input().split()
    item_name = " ".join(map(str,item[:len(item) - 1]))
    if item_name in items_prices:
        items_prices[item_name] += int(item[len(item) - 1])
    else:
        items_prices[item_name] = int(item[len(item) - 1])

for item_name, price in items_prices.items():
    print(f"{item_name} {price}")
