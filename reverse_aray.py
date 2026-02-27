#  Methods of Reversing the elements in Array

# Reversing using slicing 
arr = [2,4,5,6]
reverse = arr[::-1]
print(reverse )

# Using reverse()
arr1 = [3,4,6,7]
arr1.reverse()
print(arr1)

# 2-Pointer method
a = [1,2,3,4]
i = 0            #1 element
j = len(a) -1    #last element

while i<j:
    a[i],a[j] = a[j],a[i]      #tuple packaging
    i += 1             # moving left side 
    j -=1               # moving right side 
print(a)