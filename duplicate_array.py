nums = [1,2,3,1]
def duplicate(nums):
    freq = {}
    for num in nums:
        if num in freq:
            return True
        else:
            freq[num] = 1
    return False
print(duplicate(nums))
    
