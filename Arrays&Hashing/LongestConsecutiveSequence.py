# LC 128: Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Yzer De Gula

from typing import List

"""
Question:
  Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
  
  You must write an algorithm that runs in O(n) time.

 
Example 1:
  Input: nums = [100,4,200,1,3,2]
  Output: 4
  Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
  Input: nums = [0,3,7,2,5,8,4,6,0,1]
  Output: 9
 

Constraints:
  0 <= nums.length <= 105
  -109 <= nums[i] <= 109

U-nderstand:
  - What is the input?
      The input is an UNSORTED array of INTEGERS
  - What is the output?
      The output is an integer representing the length of the longest consecutive
      elements sequence
  - Can the input array be empty?
      No, the problem's constraints state that the length of the array can range
      from 0 to 10^5
  - Are duplicates allowed in the longest length?
      I don't believe anywhere in the problem or its contraints that acknowledges
      duplicates. But I think that we should factor this in, as it make sense that
      only distinct elements count in the longest sequence

  Happy Case:
  Input: nums = [1,2,10,11,12]
  Output: 3

  Edge Case:
  Input: nums = []
  Output: 0


M-atch:
  For arrays and strings, common solution patterns include:
    - Sort
    - Two Pointer Solution
    - Storing the elements of the array in a HashMap or a Set
    - Traversing the array with a sliding window

  Sorting can help us in solving this problem, by having elements ascending in
  sequential order, making it easier for us to get the length of consecutive 
  sequences. We can keep track of the longest and the current sequence, 
  iterating over the array and seeing if a duplicate of the current element 
  exists. Then checking if the next value in the sequence differs by one and
  incrementing the length. Then setting the longest sequence by checking 
  the max between the current longest sequence and the current sequence

  Two Pointer Solution nor Sliding Window I think would help in solving this
  problem. However, I think storing the elements in a HashMap or a Set can 
  help. I think what we can do is store the elements in a Set, do skip over
  checking for duplicates altogether, due to the nature of sets. After that
  we can iterate over the length of the input array, and check if the 
  current value in the array has a left number present in the set, if it
  doesn't have a left number present it means that this value is the start
  of the sequence. We would then have a while loop check if the current 
  number + the current length number is present in the set. After we would
  do the comparison between the current longest sequence and the current
  sequence

P-lan:
  Plan 1: (Sort)
    1) Sort the array 
    2) Declare our variables to keep track of the longest sequence and the
       current one
    3) Iterating over the length of the array
    4) Check if the current value is equal to the previous value, if so,
       continue to the next iteration
    5) If the current number is 1 greater than the previous number, increment
       the current length 
    6) If it doesn't take the max of the current longest sequence and this 
       current sequence
    7) Return the longest sequence

  Plan 2: (HashMap / Set)
    1) Store the nums array into a set
    2) Declare our variables to keep track of the longest sequence and the
       current one
    3) Iterating over the length of the array
    4) If the current value - 1 is not in the set, set the current length to 0
    5) Otherwise, while the current value + 1 is in the set, increment the 
       current length by 1
    6) Take the max between the current longest sequence and the current sequence
    7) Return the sequence


I-mplement:
"""

def longestConsecutive(nums: List[int]) -> int:
    # Put the values of the nums array into a set
    nums_set = set(nums)

    # Declare our variables to compare the length of the longest and current sequence
    longest_length = 0
    current_length = 0

    # Itearting over the length of our array
    for i in nums:
        # if the element doesn't have a number before it, it marks the start of the sequence
        if i - 1 not in nums_set:
            current_length = 0
            # While there a consecutive number
            while i + current_length in nums_set:
                # Increment the length of the current sequence
                current_length += 1
        # Set the longest length to the max of the current longest length and the current length
        longest_length = max(longest_length, current_length)
        
    # Return the longest length
    return longest_length

# Expects 4
nums_1 = [100,4,200,1,3,2]
print(longestConsecutive(nums_1))

# Expects 9
nums_2 = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums_2))

# Expects 0
nums_3 = []
print(longestConsecutive(nums_3))
