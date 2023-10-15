# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

# Arrow Up
for i in range(1,n+1):
    arrow = 'H' * (2 * i - 1)
    print(arrow.center(2*n))

# H letter upper
for i in range(n + 1):
    spaces = ' ' * 2 * n
    row_H = ('H' * n) 
    print(row_H.center(2*n) + spaces + row_H.center(2*n) + spaces)    
    
    

# H letter middle
for i in range(int((n + 1)/2)):
    row_H = ('H' * 5*n) 
    print(row_H.center((6)*n))        

# H letter down 
for i in range(n + 1):
    spaces = ' ' * 2 * n
    row_H = ('H' * n) 
    print(row_H.center(2*n) + spaces + row_H.center(2*n) + spaces)    


# Arrow Down
for i in range(n, 0, -1):
    spaces = ' ' * 4 * n
    arrow = 'H' * (2 * i - 1)
    print(spaces + arrow.center(2*n))
