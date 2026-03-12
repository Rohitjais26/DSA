s = "anagram" 
t = "nagaram"

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    freq = {}

    for char in s:
        freq[char] = freq.get(char,0)+1

        for char in t:
            if char not in freq:
                return False
            else:
                freq[char] -=1
                return True
print(isAnagram(s,t))