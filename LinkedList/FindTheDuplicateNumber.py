# LC 287: Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array of integers, named nums containing n + 1 integers
    where each integer is in the range [1, n] inclusive.
    # ? What is our output ?
        Our output is the repeated number in the array
    # ? Can there be multiple repeated numbers ?
        No, the problem emphasizes that there is only one repeated number in 
    the input array.
    # ? Are there any restrictions on runtime or memory ?
        Yes, we must solve the problem without modifying the array nums and
    uses only constant extra space.

M-atch:
    For arrays and strings common patterns for solutions include:
        1) Store in Hash Map or Set
        2) Sorting
        3) Two Pointers
        4) Sliding Window
    
        Disregarding the restrictions for memory, we can naively solve this
    problem by storing the elements in a set. We will iterate over the input
    array and then check if the element is in our set, if so, return that
    number, if not, add it to our set. 

P-lan:
    Naive Solution:
        1) Declare our set
        2) Iterating over the input array
        3) Check if the element is in our set
        4) If so, return that element
        5) Otherwise, add that element to the list


I-mplement:
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Declare our set
        nums_set = set()

        # Iterate over the input array
        for num in nums:
            # If the element is in the set already, we've found the duplicate
            if num in nums_set:
                # Return that number
                return num
            # Otherwise, the number isn't in the set already
            else:
                # Add the number to the set
                nums_set.add(num)


    def findDuplicateOptimal(self, nums: List[int]) -> int:
        # There are two parts of Flyod's algorithm, the first part using a slow and
        # fast pointer to find where they intersect, this marks the start of the 
        # cycle. The second part uses two slow pointers, one at the previously 
        # calculated cycle start and the other at the head of the list, the proof
        # shows that the intersection of these two pointers, is the duplicate vaule
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.findDuplicate(nums)}")
        print(f"        {self.findDuplicateOptimal(nums)}\n")  


# Testing
test = Solution()


# Expects 2
nums = [1,3,4,2,2]
test.display(nums)

# Expects 3
nums = [3,1,3,4,2]
test.display(nums)