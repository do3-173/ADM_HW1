def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for number in l:
            formatted_number = '+91 ' + number[-10:-5] + ' ' + number[-5:]
            formatted_numbers.append(formatted_number)
        f(formatted_numbers)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 