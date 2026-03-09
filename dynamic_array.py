# dynamic array - A dynamic array is an array-like data structure that can grow or shrink in size automatically as you add or remove elements.
# How it works internally
# Suppose the dynamic array starts with capacity 4.
# It may look like this:
# [10, 20, 30, 40]
# Now you want to add 50, but the array is full.
# So internally:
# a new larger block of memory is created, often double the size
# old elements are copied into the new block
# the old memory is discarded
# new element is added

#apend, modulo for safe indexing, XOR, zero indexed array, list of lists
# Approches: Direct simulation using list of lists(done here), 

# So the process is:
#read one query
#execute that query
#update state
#move to next query
# This is called sequential processing.

#Final conclusion
#So the reason we use if-else is:
#Each query has a type
#Type 1 and type 2 have different operations
#One query line can only be one type at a time
#Therefore only one corresponding block of code should run
#if-else is the programming tool used to choose between these two possible actions


def dynamicArray(n, queries):
    # Write your code here
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for q, x, y in queries:
        idx = (x ^ lastAnswer) % n

        if q == 1:
            arr[idx].append(y)
        else:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
            return answers