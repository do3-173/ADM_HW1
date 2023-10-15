# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict

n = int(input())

distinct_words = OrderedDict()
for _ in range(n):
    word = input()
    if word in distinct_words:
        distinct_words[word] += 1
    else:
        distinct_words[word] = 1
    
print(len(distinct_words.items()))
print(" ".join(map(str, [num for word, num in distinct_words.items()])))
