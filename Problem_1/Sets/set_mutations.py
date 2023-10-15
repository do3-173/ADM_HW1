# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
a_set = set(map(int,input().split()))
n = int(input())
for i in range(n):
    command = input().split()
    n_set = set(map(int,input().split()))
    if command[0] == 'intersection_update':
        a_set.intersection_update(n_set)
    elif command[0] == 'symmetric_difference_update':
        a_set.symmetric_difference_update(n_set)
    elif command[0] == 'difference_update':
        a_set.difference_update(n_set)
    elif command[0] == 'update':
        a_set.update(n_set)

print(sum(a_set))
