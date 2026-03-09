# Sparse arrays problem
# Count how many times each query string occurs. Is this string exactly equal to an element in stringList?
# Exact matching is required, so a query string of "abc" will not match an input string of "abcc" or "aabc".

# concepts:
#Arrays / Lists - A list is an ordered collection of values, duplicates are allowed. (That matters because we are counting occurrences.)
#Strings - A string is a sequence of characters. (A string comparison checks whether both strings are exactly the same.)
#Frequency counting - look down (How many times something appears)

#Searching - linear search (check each element one by one, if there are many queries, scanning again and again becomes slow.)
# binary search (requires sorted data), hash maps/dictionaries (key-value pairs for fast lookups)
#Hash maps / Dictionaries (in python dict store data as key -> value)
#For this problem:
#key = string
#value = number of times it appears, so if we create something like
 #  {
 #   "aba": 2,
 #   "baba": 1,
 #   "xzxb": 1
 #   } is This is called a frequency map or hash map.

#Trade-off between preprocessing(Do some work once in advance so that later questions become easy to answer.)- look above how we craeted the frequency map
# and repeated searching
# We first build a frequency table from stringList.Then each query is answered quickly.

# frequency idea appears in many DSA problems:
#counting characters
#counting numbers
#finding duplicates
#checking anagrams
#most frequent element
#grouping items

# Core logic : Count all strings once using a dictionary, then answer each query using dictionary lookup.
# approches: 
#1. Brute force: For each query, scan through stringList and count occurrences. O(q * n) time complexity.
def matchingStrings(stringList, queries):
    result = []
    
    for q in queries:
        count = 0
        for s in stringList:
            if s == q:
                count += 1
        result.append(count)
    
    return result
#2. Frequency map: Create a frequency map of stringList, then for each query, look up the count in the map. O(n + q) time complexity.
def matchingStrings(stringList, queries):
    freq = {}
    
    for s in stringList:
        if s in freq:
            # if we have already seen this string before, add 1
            freq[s] += 1
        else:
            # otherwise start its count at 1
            freq[s] = 1
    
    result = []
    for q in queries:
        result.append(freq.get(q, 0))
    
    return result
#3. Python’s built-in count()
# It looks shorter, but internally count() still scans the whole list. So for each query, it does a full traversal. O(q * n) time complexity, 
# same as brute force, but more concise.
def matchingStrings(stringList, queries):
    result = []
    for q in queries:
        result.append(stringList.count(q))
    return result
# 4. Using collections.Counter
# What Counter does
#If:
#Counter(["aba", "baba", "aba", "xzxb"])
#It becomes roughly:
#  {
 #   "aba": 2,
 #   "baba": 1,
 #   "xzxb": 1
 #  }
# So Counter is basically a specialized dictionary for counting.

from collections import Counter

def matchingStrings(stringList, queries):
    freq = Counter(stringList)
    return [freq[q] for q in queries]

# 5. Sorting + binary search

# 6. Memoization for repeated queries
# This improves brute force somewhat when queries repeat, but it is still generally worse than frequency-map preprocessing.


# additional topics:
# maps vs dict
# why hash is fatser than dict
# hashing mechanism