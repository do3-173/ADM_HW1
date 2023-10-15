import textwrap

def wrap(string, max_width):
    i = max_width
    while i < len(string):
        string = string[0:i] + '\n' + string[i:len(string)]
        i += max_width + 1
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)