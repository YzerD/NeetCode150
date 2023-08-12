# LC 153: Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ? 
        Our input is an integer array named nums, and is sorted in ascending
    order and is rotated between 1 and n times.
    # ? What is our output?
        Our output is the minimum element of the rotated array
    # ? Can our input array be empty ?
        No, the constraints of the problem states that the minimum number of
    elements we can have in our array is 1.
    # ? What happens if the array is rotated n times ?
        If the input array is rotated n times, that means that the array has
    been shifted to its original position. 
    # ? Is there any restrictions on the runtime of our solution ?
        The problem specifies that we must write an algorithm that runs in 
    O(log n) time. 

    
M-atch:
    Considering that the problem specifies that our algorithm's runtime must be
O(log n) and we're searching for an element, we must utilize binary search.
We can first declare our left and right pointers for the binary search, as well
as a variable to keep track of our minimum. Then, while our pointers haven't 
crossed, calculate the middle index and set the current minimum to that. Then
we can check if the value at the middle index is greater than the right pointer,
if this is the case, we know that the minimum lies somewhere in the right of the
array. Otherwise, we know that the minimum lies somewhere in the left of the
array. Then outside of the while loop we can return the minimum of the current
minimum and the value held at the left pointer.


P-lan:
    1) Declare our left and right pointers
    2) Declare our current min variable set to the max value possible
    3) While our left and right pointers haven't crossed
    4) Calculate the middle index
    5) Set the current minimum to the value held a the middle index
    6) If the value at the middle is greater than the value at the end
       We know that the minimum lies somewhere in the right of the array,
       and we'd update our left pointer to middle + 1
    7) Otherwise, we know that the minimum lies somewhere in the left of
       the array.
    8) We would then return the minimum of the current minimum and the value
       held at the left pointer.

I-mplement:
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Declare our left and right pointers
        left, right = 0, len(nums) - 1

        # Declare our current minimum
        curr_min = float("inf")

        # While our pointers haven't crossed
        while left < right:
            # Calculate middle index
            middle = (left + right) // 2

            # Take the min of the current min and the value at the middle
            curr_min = min(curr_min, nums[middle])

            # Check to see if the value held at the middle is greater than
            # the value at the right
            if nums[middle] > nums[right]:
                # Then we know that the minimum lies somewhere in the right side
                left = middle + 1
            # Otherwise, we know that the minimum lies somewhere in the left side
            else:
                # Update our right pointer
                right = middle - 1
            
        # We can then return the min of the current min and the value at the start
        return min(curr_min, nums[left])


    
    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output:       {self.findMin(nums)}\n")


# Testing
solution = Solution()


# Expects 1
nums = [3,4,5,1,2]
solution.display(nums)

# Expects 0
nums = [4,5,6,7,0,1,2]
solution.display(nums)

# Expects 11
nums = [11,13,15,17]
solution.display(nums)