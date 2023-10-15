def print_rangoli(size):
    letter_num = ord('a') + size - 1
    rangoli = chr(letter_num)
    
    print(rangoli.center(4*size-3, '-'))
    for i in range(1, size):
        rangoli = rangoli[0:len(rangoli)//2+1] + '-' + chr(letter_num - i) +  '-' + rangoli[len(rangoli)//2:len(rangoli)] 
        print(rangoli.center(4*size-3, '-'))
    
    for i in range(size - 1):
        rangoli = rangoli[0:len(rangoli)//2-2] + rangoli[len(rangoli)//2+2:len(rangoli)]
        print(rangoli.center(4*size-3, '-'))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)