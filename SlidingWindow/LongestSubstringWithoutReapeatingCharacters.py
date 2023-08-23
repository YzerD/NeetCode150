# LC 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Yzer De Gula


"""
U-nderstand:
    # ? What is our input ?
        Our input a string, s.
    # ? What is our output ?
        Our output is the length of the longest substring without reapting 
    characters.
    # ? What is a substring ?
        A substring is a contiguous non-empty sequence of characters within
    a sting.
    # ? Can our input string be empty ?
        Yes, the constraints state that the length of the input string can 
    range from 0 to 50,000.
    # ? Is our input string purely alphabetical ?
        No, the input string can consist of English letters, digits, symbols,
    and spaces.
    # ? Are there any restrictions on runtime or memory ?
        No, the problem doesn't explicitly specify any runtime or memory 
    restrictions. 

    
M-atch:
    For arrays and strings, common patterns for solutions include:
        1) Sorting
        2) Two Pointers
        3) Storing in a Hash Map or Set
        4) Sliding Window

        For this problem, knowing that we're looking for non-repeating
    characters, we can use a set to keep track of distinct characters. Sorting
    wouldn't help. We can use Sliding Window since we want to see the sections
    of the input string to see if they're the longest substring. We could also
    utilize two pointers to keep track of the size of our window. This is 
    because as we iterate further in the string and we see a duplicate, we can
    remove the character from the left side and increment that. Otherwise, we
    haven't seen it and we can add it to our set and update our result. 

        
P-lan:
    1) Declare our set
    2) Decalre our left pointer and result
    3) Iterating over the length of the array
    4) While the character held by the right pointer is in our set
        a) Remove the character held by the left pointer
        b) Increment our left pointer
    5) Otherwise, we know that the character is not a duplicate
        a) Add character held by the right pointer to the set
        b) Update our result variable by taking the max of the current max and
           the length of our window (right - left + 1)
    6) Return result variable


I-mplement:
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Declare our variables
        charSet = set()
        left = 0
        result = 0

        # Iterating over the length of the input array
        for right in range(len(s)):
            # While the character held in the right pointer is in our set
            while s[right] in charSet:
                # Remove the character held in the left pointer from our set
                charSet.remove(s[left])
                # Increment our left pointer
                left += 1
            # Otherwise, we know that the character isn't a duplicate and add it to set
            charSet.add(s[right])
            # Update our result
            result = max(result, right - left + 1)
        # Return result
        return result


    def display (self, s: str) -> None:
        print(f"Input: s = {s}")
        print(f"Output:    {self.lengthOfLongestSubstring(s)}\n")


# Testing
test = Solution()


# Expects 3
test.display(s = "abcabcbb")

# Expects 1
test.display(s = "bbbbb")

# Expects 3
test.display(s = "pwwkew")
