cube = lambda x: x*x*x# complete the lambda function 



def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib_array = [0, 1]
    i = 2
    while i < n:
        fib_array.append(fib_array[i-1] + fib_array[i-2])
        i += 1
        
    return fib_array
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))