if __name__ == '__main__':
    s = input()
    alphanum = alpha = digit = lower = upper = False
    for i in range(len(s)):
        if s[i].isalnum():
            alphanum = True
        
        if s[i].isalpha():
            alpha = True
        
        if s[i].isdigit():
            digit = True
        
        if s[i].isupper():
            upper = True
        
        if s[i].islower():
            lower = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
    
