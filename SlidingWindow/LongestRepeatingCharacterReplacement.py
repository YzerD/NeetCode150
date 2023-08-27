# LC 424: Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Yzer De Gula


"""
U-nderstand:
    # ? What is our input ?
        Our input is a string s, and an integer k.
    # ? What is our output ?
        Our output is the length of the longest substring containing
    the same letter you can get after performing the above operations.
    # ? What is the operations mentioned ?
        We can choose any character of the string and change it to any other
    uppercase English character, and we can perform this operation at most k
    times.
    # ? Can our input string include anything besides uppercase characters ?
        No, the problem states that our input string consists of only uppercase
    English letters.
    # ? Can our input be empty ?
        No, the minimum length of our input string is 1
    # ? Can k be greater than our input string?
        No, k can range from 0 to the length of our input.

M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointers
        2) Sorting
        3) Storing in a Hash Map or Set
        4) Sliding Window
    
        For this problem, sorting wouldn't help, as well as two pointers. 
    We can use a Hash Map to store the frequency of the characters, as well as
    sliding window, since problems with substrings are commonly solved with 
    sliding window. We can declare our dictionary and left pointer for the size
    of our window. We can then iterate over the length of the string, and store
    the character seen by the right pointer (which is the iterator) and add it
    if we've seen it, or return 0 if it doesn't exist in our hash map. There,
    we can calculate the size of our window which is right - left + 1 subtracting
    the max character we've seen in our map. We need to check the condition that
    this expression evaluates greater than k. This is because k is the amount of
    times we can perform the replacement operation within our substring. So if 
    the expression evaluates greater, we decrement the value of the character
    held by the left side of our window and increment our left pointer. Finally,
    we can find the max of the current max and the size of the window we just 
    calculated, and return the result


P-lan:
    1) Declare our Hash Map
    2) Declare our result variable
    3) Declare our left pointer
    4) Iterating over the entire input string
    5) Add the character held by the right pointer to the Hash Map or return 0,
       if it's not present in our Hash Map.
    6) We can then check if the size of our window minus the max character freq
       is greater than k
    7) If so, we can decrement the value held by the left pointer
    8) As well as increment the left pointer
    9) Get the max of the current max and the size of the window
    10) Return the result

I-mplement:
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create our variables
        char_map = dict()
        result = 0
        left = 0

        # Iterate over our input string
        for right in range(len(s)):
            # Add the character held by the right pointer to the Hash Map, or
            # return 0 if not present
            char_map[s[right]] = 1 + char_map.get(s[right], 0)

            # If the size of our window minus max char freq > k
            if (right - left + 1) - max(char_map.values()) > k:
                # Decrement the value held by the left pointer
                char_map[s[left]] -= 1
                # Increment left pointer
                left += 1
            
            # Get the max of the current max and the current window size
            result = max(result, right - left + 1)

        # Return result
        return result


    def characterReplacementOptimal(self, s: str, k: int) -> int:
        # Create our variables
        char_map = dict()
        result = 0
        left = 0
        max_freq = 0

        # Iterate over our input string
        for right in range(len(s)):
            # Add the character held by the right pointer to the Hash Map, or
            # return 0 if not present
            char_map[s[right]] = 1 + char_map.get(s[right], 0)

            # Get the max character frequency
            max_freq = max(max_freq, char_map[s[right]])

            # If the size of our window minus max char freq > k
            if (right - left + 1) - max_freq > k:
                # Decrement the value held by the left pointer
                char_map[s[left]] -= 1
                # Increment left pointer
                left += 1
            
            # Get the max of the current max and the current window size
            result = max(result, right - left + 1)

        # Return result
        return result
    

    def display(self, s: str, k: int) -> None:
        print(f"Input: s = {s}, k = {k}")
        print(f"Output: {self.characterReplacement(s, k)}")
        print(f"        {self.characterReplacementOptimal(s, k)}\n")


# Testing
test = Solution()

# Expects 4
test.display(s = "ABAB", k = 2)

# Expects 4
test.display(s = "AABABBA", k = 1)
