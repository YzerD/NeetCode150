# LC 75: Sort Colors (Medium)
# https://leetcode.com/problems/sort-colors/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an array called nums that has n objects, with the objects
        being colored red, white, or blue. These are represented by 0, 1, and 2
        respectively.
    - What is our output?
        Our output is the array with the colors sorted in red, white, and blue
        order.
    - Can our input be empty?
        No, the constraint's state that the minimum number of elements in the
        array is 1 and has a max of 300.
    - Can the input be outside 0, 1, and 2?
        No, the constraint's state that the elements in the input array are 0,
        1, and 2
    - Can we use the sort function?
        No, the problem states that we must solve this problem without the use
        of the sort function
    - Can we create and return a new array object?
        No, the problem asks us to solve it in-place instead of returning a new
        object.
    
    Happy Case:
    Input: nums = [2,1,0]
    Output: [0,1,2]

    Input: nums = [2,1,0,1,2,0,1,1,0]
    Output: [0,0,0,1,1,1,1,2,2]

    Edge Case:
    Input: nums = [0]
    Output: [0]

    
M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Sorting
        2) Two Pointers
        3) Sliding Window
        4) Storing in a HashMap or HashSet

    We cannot use the librarys sort function, so that rules out that approach.
    Sliding window is not useful for this one, storing in a hash map or hash
    set would complicate our solution. This leaves us with Two Pointers, but
    I think we can actually use Three of them. One representing the location
    of 0's, 1's, and 2's. We can have a left pointer, a middle pointer, and a
    right pointer. The left pointer will be where we store all our 0's, and
    the middle pointer will be for the 1's, and 2's will be for all the 1's.
    We can then have a while loop that goes on until our middle and right
    pointer haven't crossed. We then check if the middle pointer has a 0, if
    this is the case we have to update our pointers, left and middle will 
    increment. If the middle pointer has a 1, we have to update only our
    middle pointer which we would increment. Otherwise, it's a two and we
    need to update our right by decrementing. I forgot that we need to
    swap the elements before updating our pointers. 

P-lan:
    1) Declare our pointers
    2) While our middle pointer hasn't crossed with the right pointer
    3) Check if the middle pointer has a 0
    4) If so, update our left and middle pointer
    5) Check if the middle pointer has a 1
    6) If so, update our middle pointer
    7) Otherwise, the middle pointer has a 2
    8) If so, we update our right pointer

I-mplement:
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Declare our pointers
        left, middle, right = 0, 0, len(nums) - 1

        # While our middle and right pointers haven't crossed
        while (middle <= right):
            # Check if the middle pointer has a 0
            if nums[middle] == 0:
                # Swap the elements
                nums[left], nums[middle] = nums[middle], nums[left]

                # Update our left and middle pointers
                left += 1
                middle += 1

            # Check if the middle pointer has a 1
            elif nums[middle] == 1:
                # Since we don't need to swap, 1 is in the right position
                # and we just need to update our middle pointer
                middle += 1

            # Otherwise, the middle pointer has a 2
            else:
                # Swap the elements
                nums[right], nums[middle] = nums[middle], nums[right]

                # Update our right pointer
                right -= 1


    def display(self, nums: List[int]) -> None:
        print(f"Input:  nums = {nums}")
        self.sortColors(nums)
        print(f"Output:        {nums}\n")

# Testing 
solution = Solution()

# Expects [0,0,1,1,2,2]
nums = [2,0,2,1,1,0]
solution.display(nums)


# Expects [0,1,2]
nums = [2,0,1]
solution.display(nums)


# Expects [0,0,0,1,1,1,1,2,2]
nums = [2,1,0,1,2,0,1,1,0]
solution.display(nums)


# Expects [0]
nums = [0]
solution.display(nums)