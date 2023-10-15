import numpy

def arrays(arr):
    return numpy.array(sorted(arr, key = lambda x: -abs(float(x))), dtype=float)
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)