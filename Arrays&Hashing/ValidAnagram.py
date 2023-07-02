# LC 242: Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Resources Used: https://www.w3schools.com/python/python_dictionaries_access.asp
# Yzer De Gula 

"""
U-nderstand:
    - Can the input strings be empty?
        No, from the problem's contraints, it says that the minimum length of
        the input string is 1
    - Can the input strings be of different lengths?
        The problem doesn't state that both strings must be of the same length
        so that means we'll account for this case, we'd return false if they
        are of differing lengths
    - What is an anagram?
        An Anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters 
        exactly once
    - Does the position of the letters matter in the string when checking if
      it's an anagram?
        No, since an anagram is formed by rearranging the letters
    - What is our output?
        Our output is a boolean that returns true if both input strings are
        anagrams to eachother, false otherwise.

    Happy Case:
    Input: s = "apple", t = "paple"
    Output: True

    Input: s = "solution", t = "problem"
    Output: False

    Edge Case:
    Input: s = "z", t = "z"
    Output: False    

M-atch:
    For array and string problems, the most common patterns for the solutions
    are:

        1) Sorting
        2) Two Pointers
        3) Placing the Elements in a Hash Map or Set
        4) Sliding Window

    Sorting can help us by having all the characters of the strings in 
    alphabetical order and we can iterate over the length of one string
    and check if the characters at that index match. Two Pointers I 
    don't think would help, it might help if we were checking for 
    palindromes. Placing the elements in a Hash Map can help solve this
    by maybe having two maps (dicts in Python) for each string having
    the char as the key and their frequency as the value. We would then
    iterate over the map checking if the key and value match.

P-lan:
    Plan 1:
        1) Check if the lengths of the strings are not equal, if so return false
        2) Sort the strings
        3) Iterating over the length of one of the strings
        4) If for any of the chars from both strings don't match return false
        5) If after iterating we can return false since all the chars matched

    Plan 2: 
        1) Check if the lengths of the strings are not equal, if so return false
        2) Store both the strings into seperate Hash Maps, having their chars as
           the key and their frequency as the value.
        3) Iterating over one map, check the other map if the keys and values
           don't match, if this happens return false.
        4) Otherwise, return True

I-mplement:
"""
# PLAN 1: SORTING
def isAnagram(s: str, t: str) -> bool:
    # If the string's lengths are not equal
    if (len(s) != len(t)):
        # Return False
        return False
    
    # Sort the strings
    s = sorted(s)
    t = sorted(t)

    # Iterating over the length of one of the strings
    for i in range(len(s)):
        # If the chars don't match
        if s[i] != t[i]:
            # Return False
            return False
    
    # Otherwise return True
    return True


# PLAN 2: HASHING
def isAnagramHashing(s: str, t: str) -> bool:
    # Check if the string's lengths differ
    if (len(s) != len(t)):
        return False

    # Declare our maps
    s_map = dict()
    t_map = dict()

    # For the length of the first string
    for i in s:
        # If the char is already in the map
        if i in s_map:
            # Increment it
            s_map[i] += 1
        # Otherwise,
        else:
            # Add it to the map
            s_map[i] = 1
    
    # Repeat for second string
    for i in t:
        if i in t_map:
            t_map[i] += 1
        else:
            t_map[i] = 1
    
    # Iterating over the items in the first map
    for key,value in s_map.items():
        # If the key or the values don't match
        if (key not in t_map) or (value != t_map[key]):
            # Return False
            return False
    
    # Otherwise return True
    return True

# TEST CASES
string_1, string_2 = "anagram", "nagaram"
# Expects True
# print(isAnagram(string_1,string_2))
print(isAnagramHashing(string_1, string_2))


string_3, string_4 = "rat", "car"
# Expects False
# print(isAnagram(string_3, string_4))
print(isAnagramHashing(string_3, string_4))


string_5, string_6 = "z", "z"
# Expects True
# print(isAnagram(string_5, string_6))
print(isAnagramHashing(string_5, string_6))

"""
R-eview:
    I think between the two plans the one I had to review how to access the key
value pairs in a Python Hash Map. You can use item() to get the key value as a
tuple. 

E-valuate:
    For Plan 1 the Time Complexity is O(nlog(n)) since we used the sorting
function. The Space Complexity is O(n) since we stored the sorted versions
of the strings.
    For Plan 2 the Time Complexity is O(n) since it took n steps to store
the string's characters into a map and check the key-value pairs. The Space
Complexity is O(n) since we stored the strings into Hash Maps.
"""