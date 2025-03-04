# LC 128: Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/merge-strings-alternately/
# Yzer De Gula

"""
# U-nderstand: 
    What is the input?
        Our input are two strings word1 and word2
    What is our output?
        Our output is the merged string between the two. We START with word1, and if a
        string (word1 or word2) is longer than the other, append the additional letters
        onto the end of the merged string.
    What kind of characters can our input strings consist of?
        According to the constraint's, our input strings consist of ONLY lowercase
        English letters. Also, our input strings can range from 1 to 100, meaning that
        the input string(s) cannot be empty.

# M-atch:
    For strings and arrays, common patterns include:
        - Sorting
        - Sliding Window
        - Two Pointer
        - Hash Set / Map

    Considering the nature of the problem, sorting would disturb the arrangement
    of the characters in the string, sliding window and two pointer don't really
    make sense, nor does a hash map.

    So what I'm thinking is that we take the minimum between the length of the 
    two input strings and have a for loop run for that length. Then we get the
    larger string and append the rest of it to the merged string.

# P-lan:
    1.) Create a variable, set to get the minimum length of the input strings
    2.) Create a variable, set to the larger string
    3.) Create a variable to store our merged string
    4.) Iterating for the length of the shorter string
    5.) Append the first letter from the first string
    6.) Append the second letter from the second string
    7.) After the loop append the rest (if it exists) of the larger string
    8.) Return the merged string

# I-mplement:
"""

def mergeAlternately(word1: str, word2: str) -> str:
    # Create a variable to get the length of the shorter string
    shorter_length = min(len(word1), len(word2))

    # Create a variable to get the larger string
    larger_string = word1 if len(word1) > len(word2) else word2

    # Create a variable to store our solution
    merged_string = ""

    # Iteraeting for the length of the shorter string
    for i in range(shorter_length): 
        # Append a character from word1 to the merged string
        merged_string += word1[i]

        # Append a character from word2 to the merged string
        merged_string += word2[i]

    # After the loop, append the rest of the larger string to the merged (if it exists)
    merged_string += larger_string[shorter_length:]

    # Return the merged string
    return merged_string

mergeAlternately("abc", "pqr")   # Expects "apbqcr"
mergeAlternately("ab", "pqrs")   # Expects "apbqrs"
mergeAlternately("abcd", "pq")   # Expects "apbqcd"