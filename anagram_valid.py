s = "anagram"
t = "nagaram"

def isAnagram(s, t):

    if len(s) != len(t):
        return False

    freq = {}

    # count characters in s
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # reduce counts using t
    for char in t:
        if char not in freq:
            return False
        
        freq[char] -= 1
        
        if freq[char] < 0:
            return False

    return True


print(isAnagram(s, t))