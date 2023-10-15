if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_arr = list(set(arr))
    unique_arr.sort(reverse=True)
    print(unique_arr[1])
