# LC 33: Search in Rotated Sorted Array
# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an integer array named nums, with distinct values and is
    sorted in ascending order and may be rotated between 1 and n times.
    # ? What is our output?
        Our output is the index of the target element in the array, or -1 if
    the target element is not in the array.
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
O(log n) and we're searching for an element, we must utilize binary search. We 
can first declare our left and right pointers for the binary search. Then, while
our pointers haven't crossed, calculate the middle index and check if the value
at the middle index is equal to the target. If this is the case, we can return
the middle index. Otherwise, we can check if the value at the middle index is
greater than the value at the right pointer. If so we can update our left pointer
to middle + 1, otherwise we can update our right pointer to middle - 1. Outside
of the while loop we can return -1, as the target element is not in the array.

P-lan:
    1) Declare our left and right pointers
    2) While our left and right pointers haven't crossed
    3) Calculate the middle index
    4) If the value at the middle index is equal to the target
       We can return the middle index
    5) Otherwise, if the value at the middle index is greater than the value
       at the right pointer, we can update our left pointer to middle + 1
    6) Otherwise, we can update our right pointer to middle - 1
    7) Outside of the while loop we can return -1, as the target element is
       not in the array.

I-mplement:
"""

class Solution:
    # Passes 120/195 test cases
    def search(self, nums: List[int], target: int) -> int:
        # Declare our left and right pointers
        left, right = 0, len(nums) - 1

        # While our left and right pointers haven't crossed
        while left <= right:
            # Calculate the middle index
            middle = (left + right) // 2

            # If the value at the middle index is equal to the target
            if nums[middle] == target:
                # We can return the middle index
                return middle
            # Otherwise, if the value at the middle index is greater than the
            # value at the right pointer
            elif nums[middle] > nums[right]:
                # We can update our left pointer to middle + 1
                left = middle + 1
            # Otherwise, we can update our right pointer to middle - 1
            else:
                right = middle - 1

        # Outside of the while loop we can return -1, as the target element is
        # not in the array.
        return -1
    

    def searchNeetCode(self, nums: List[int], target: int) -> int:
        # Declare our left and right pointers
        left, right = 0, len(nums) - 1

        # While our left and right pointers haven't crossed
        while left <= right:
            # Calculate the middle index
            middle = (left + right) // 2

            # If the value at the middle index is equal to the target
            # Return the index
            if nums[middle] == target:
                return middle
            
            # We can then check if the target lies somewhere in the left of the array
            if nums[middle] >= nums[left]:
                # Check if the middle is less than the target and the target
                # is less than the left pointer
                if nums[middle] < target or target < nums[left]:
                    # Update our left pointer to middle + 1
                    left = middle + 1
                # Otherwise, update our right pointer to middle - 1
                else:
                    right = middle - 1


            # Otherwise, the target lies somewhere in the right of the array
            else:
                # Check if the middle is greater than the target and the target 
                # is greater than the right pointer
                if nums[middle] > target or target > nums[right]:
                    # Update our right pointer to middle - 1
                    right = middle - 1
                # Otherwise, update our left pointer to middle + 1
                else:
                    left = middle + 1

        # Outside of the while loop we can return -1, as the target element is
        # not in the array.
        return -1
            

    def display(self, nums: List[int], target: int) -> None:
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {self.search(nums, target)}")
        print(f"Output: {self.searchNeetCode(nums, target)}\n")


# Test Cases
test = Solution()


# Expects 4
test.display([4,5,6,7,0,1,2], 0)

# Expects -1
test.display([4,5,6,7,0,1,2], 3)

# Expects -1
test.display([1], 0)

# Expects 1
test.display([1,3], 3)
