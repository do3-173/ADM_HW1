def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique_string = ''
        for letter in string[i:i+k]:
            if letter not in unique_string:
                unique_string += letter
        print(unique_string)
    # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)