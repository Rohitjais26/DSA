# left rotation
# circular array, and index movement in it
# Modulo (Wrap around) - Modulo tells you “how far you are into the current cycle.”
# Mapping idea in left rotation : new_index = (current_index - d) % n
# new[i] = old[(i+d)%n] vs new[(i-d)%n] = old[i]
# approaches to solve: Brute force, Index mapping, Slicing, reversal algorithm

# Wrap-around example
# Using arr=[1,2,3,4,5], d=2, n=5
#Let’s fill each result[i]:

#i=0 → (0+2)%5 = 2 → arr[2]=3 → result[0]=3
#i=1 → (1+2)%5 = 3 → arr[3]=4 → result[1]=4
#i=2 → (2+2)%5 = 4 → arr[4]=5 → result[2]=5
#i=3 → (3+2)%5 = 0 → arr[0]=1 → result[3]=1 ✅ wrapped!
#i=4 → (4+2)%5 = 1 → arr[1]=2 → result[4]=2 ✅ wrapped!
#Final:
#result = [3,4,5,1,2]


# index mapping approach
def rotateLeft(d, arr):
    n = len(arr)
    d %= n
    result = [0] * n     # Creates an Array with zero values
    for i in range(n):
        result[i] = arr[(i + d) % n]
    return result