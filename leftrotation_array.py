# left rotation
# circular array, and index movement in it
# Modulo (Wrap around) - Modulo tells you “how far you are into the current cycle.”
# Mapping idea in left rotation : new_index = (current_index - d) % n
# new[i] = old[(i+d)%n] vs new[(i-d)%n] = old[i]
# approaches to solve: Brute force, Index mapping, Slicing, reversal algorithm


# index mapping approach
def rotateLeft(d, arr):
    n = len(arr)
    d %= n
    result = [0] * n
    for i in range(n):
        result[i] = arr[(i + d) % n]
    return result