# LC 78: Subsets
# https://leetcode.com/problems/subsets/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an integer array nums of unique elements
    # ? What is our output ?
        Our output is all possible subsets of our input in a list
    # ? What is a subset ?
        A subset of an array is a selection of elements (possibly none)
    of the array.
    # ? Can our input array be empty ?
        No, the constraints of the problem states that the minimum length that our
    input array can be is 1
    # ? Can we have duplicate values in our input array ?
        No, the constraints of the problem states that every number in our 
    input array is unique
    # ? What values can the elements in our input array have ?
        The constraints state that the possible values that our elements in our
    input array can take is -10 to 10.

M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointers
        2) Hash Map or Hash Set
        3) Sorting
        4) Sliding Window
    
        For this problem.


P-lan:


I-mplement:
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass


    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.subsets(nums)}\n")


# Testing
test = Solution()

# Expects [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1,2,3]
test.display(nums)

# Expects [[],[0]]
nums = [0]
test.display(nums)