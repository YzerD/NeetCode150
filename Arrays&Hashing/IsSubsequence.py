# LC 128: Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/is-subsequence/
# Yzer De Gula

"""
# U-nderstand:
    What is our input?
        Our input is a string s and a string t.
    What is our output?
        Our output is a boolean, True if t is a subsequence of s, and False
        otherwise.
    What is a subsequence?
        A subsequence is a sequence that can be derived from another sequence
        by deleting some elements without changing the order of the remaining
        elements.
    Can our input strings be empty?
        Yes, the constraints state that the length of the input strings can
        range from 0 to 104.
    Are our input strings purely alphabetical?
        Yes, the input strings can consist of only lowercase English letters
    Are there any restrictions on runtime or memory?
        No, the problem doesn't explicitly specify any runtime or memory
        restrictions.

# M-atch:
    For strings and arrays, common patterns include:
        - Sorting
        - Sliding Window
        - Two Pointer
        - Hash Set / Map

    Considering the nature of the problem, sorting would disturb the
    arrangement of the characters in the string, sliding window and two pointer
    don't really make sense, nor does a hash map.

    What we can do is first handle any edge cases, that being checking if the subsequence,
    s is larger than t. This is because we can't have a subsequence of a string that's
    smaller, so we would return false. 

    After this, we can have to iterators i and j, starting at the beginning of each string.
    and while i is less than the length of s and j is less than the length of t,we check if 
    at both indicies if the characters are the same, if so we increment each iterator. 
    If not, that means the index at t is not the same character and we'd increment j. After
    the while loop if i is equal to the length of s, we return true, if not we return False.

# P-lan:
    1.) Create our variables that get the lengths of the input strings
    2.) Create our iterators i and j
    3.) While i < len(s) and j < len(t)
    4.) Check if the character at each index is the same
    5.) If they are, increment each pointer
    6.) If not, increment j
    7.) If the i equals the len(s) we return True
    8.) Other wise, we'd return False

# I-mplement:
"""

def isSubsequence(s: str, t: str) -> bool:
    # Create our variables to get the lengths of our input strings
    length1, length2 = len(s), len(t)

    # Edge Case:
    if (length1 == 0): return True

    # Create our iterators
    i, j = 0, 0

    # Iterating over the length of t
    while (j < length2):
        # Check if the characters at the indices are the same
        if s[i] == t[j]:
            # Increment i
            i += 1
            # Check if we've matched the string
            if (i == length1): 
                return True
        # Otherwise, increment j
        j += 1
    
    # Otherwise, return false
    return False

# Testing 
print(isSubsequence("abc", "ahbgdc"))       # Expects True
print(isSubsequence("axc", "ahbgdc"))       # Expects False