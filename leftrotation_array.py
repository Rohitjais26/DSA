def rotateLeft(d,arr):
    n = len(arr)     
    d%= n
    result = [0]*n   # creating an empty array
    for i in range(n):
        result[i] = arr[(i *d)%n]
    return result
