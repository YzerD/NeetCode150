# LC 136: Single Number
# https://leetcode.com/problems/single-number/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is a non-empty array of integers, nums, where every element
    appears twice except for one.
    # ? What is our output ?
        Our output is the single number that has no duplciates.
    # ? Are there any runtime or memory restrictions ?
        Yes, the problem specifies that we must implement a solution with
    linear runtime complexity and use only constant extra space.
    # ? Is it guranteed for a single number to exist ?
        Yes, the problem specifies that the elements in the array appears twice
    except for one element which appears only once.

M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointer
        2) Storing in a Hash Map or Set
        3) Sliding Window
        4) Sorting

        From these patterns, if space wasn't restricted we could have easily
    used a Hash Set to solve this problem. For this solution we can check if the
    element is in the set, if so, remove it from the set, otherwise we would add
    it to the set. We'd then return the single element in the set, since we
    removed all the elements that appeared twice.
        But, for this solution we can implement the XOR operator, which is ^ in
    Python. The reason for this is because every number in a computer can be
    represented in binary, and since there are numbers that appear twice, they
    would have the same binary representation, and with the XOR operator we
    know that it'll evaluate to 0. This is because 0 ^ 0 = 0 and 1 ^ 1 = 0.
    Then since we know that the elements that appeared twice will evaluate
    to 0, the single number, n, will have the XOR operation, n ^ 0 = n. This
    evaluates to n since it is guranteed that a single number exists.


P-lan:
    Plan 1 (HashSet):
        1) Create our set
        2) Iterating over the input array
            i) If the number is in the Set, remove it
            ii) Otherwise, add it to the set
        3) Return the element in the set
    
    Plan 2 (Bit Manipulation):
        1) Create our result variable that's set to 0
        2) For every number in our input array
            i) Update result by taking xor operation of current num with result
        3) Return result


I-mplement:
"""

class Solution:
    def singleNumberSet(self, nums: List[int]) -> int:
        # Create our set
        result = set()

        # Iterating over the input array
        for num in nums:
            # If the number is already in our set
            if num in result:
                # Remove it
                result.remove(num)
            else:
                # Otherwise add it to the set
                result.add(num)
        
        # Return result
        return list(result)[0]


    def singleNumber(self, nums: List[int]) -> int:
        # Create our result variable and set it to 0
        result = 0
        
        # Iterating over every number in our input
        for num in nums:
            # Update result by takign xor of num and result
            result = num ^ result
        
        # Return result
        return result


    def display(self, nums: List[int]) -> int:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.singleNumberSet(nums)}")
        print(f"        {self.singleNumber(nums)}\n")  


# Testing
test = Solution()

# Expects 1
test.display(nums = [2,2,1])

# Expects 4
test.display(nums = [4,1,2,1,2])

# Expects 1
test.display(nums = [1])