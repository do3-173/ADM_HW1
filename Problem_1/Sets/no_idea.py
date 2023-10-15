# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
n_array = input().split()
A_integer = set(input().split())
B_integer = set(input().split())

happiness = 0

for i in n_array:
    if i in A_integer:
        happiness += 1    
    if i in B_integer:
        happiness -= 1
        
print(happiness)
