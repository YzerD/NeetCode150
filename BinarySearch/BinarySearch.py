# LC 704: Binary Search (Easy)
# https://leetcode.com/problems/binary-search/
# Yzer De Gula

from typing import List

"""
Question:
  Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
  
  You must write an algorithm with O(log n) runtime complexity.


Example 1:
  Input: nums = [-1,0,3,5,9,12], target = 9
  Output: 4
  Explanation: 9 exists in nums and its index is 4

Example 2:
  Input: nums = [-1,0,3,5,9,12], target = 2
  Output: -1
  Explanation: 2 does not exist in nums so return -1
 

Constraints:
  1 <= nums.length <= 104
  -104 < nums[i], target < 104
  All the integers in nums are unique.
  nums is sorted in ascending order.


U-nderstand:
  - Can the input array be empty?
      No, there will always be at least one number
  - What is the space and time complexity? 
      We want O(log(n)) time and O(1) space

  Happy Case:
  Input: nums = [-1, 0, 3, 5, 9, 12]
  target = 9
  Output: 4

  Input: nums = [-1, 0, 3, 5, 9, 12]
  target = 2
  Output: -1

  Edge Case:
  Input: nums = [-1], target = -1
  Output: 0
  

M-atch:
For Array problems, we want to consider the following approaches:
  Sort
    The arrays are already sorted.
    
  Two pointer solutions (left and right pointer variables):
    We can have a left and right pointer to create a mid point where we can decide whether or not the number exist in the left half or right half, with each iteration we find our number or exhaust our array.
    
  Storing the elements of the array in a HashMap or a Set:
  A HashMap or set just complicates our code.
  
    Traversing the array with a sliding window.
  A sliding window doesn’t really help us here.


P-lan:
  Use two pointer variables: one at the start, one at the end
  Check if the left pointer is less than the right pointer
    If not, return -1
    Else continue to next iteration
  Calculate the midpoint
    Add the left and right pointer indices, then floor divide by 2
    0 + 5 // 2 = 2
    Midpoint is 2, value is 3
  Check if the midpoint is greater than or less than the target
    If greater than, move the right pointer, left of midpoint
    If less than, move the left pointer, right of midpoint
  

I-mplement:
  1) find the starting and ending point of the array
  2) while loop of left <= right 

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # Declare our left and right pointers
      left, right = 0, len(nums) - 1

      # While our two pointers haven't crossed
      while (left < right):
        # Calculate midpoint 
        middle =  left + (right - left) // 2
        # Check if the target is in the midpoint 
        if(nums[middle] == target):
          return middle
        # Check if midpoint is less than target
        elif(nums[middle] < target):
          left = middle + 1
        # Otherwise, the midpoint is greater than target
        else:
          right = middle - 1


      return -1; 
          