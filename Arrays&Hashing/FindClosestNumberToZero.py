# LC 2239: Find Closest Number To Zero
# https://leetcode.com/problems/find-closest-number-to-zero/
# Yzer De Gula

from typing import List

"""
# U-nderstand:
    What is our input?
        Our input is and array nums of size n, n can range from 1 to 1000.
    What is our output?
        Our output is the number with the value closest to 0. Another factor we have
        to keep track of is if there are multiple answers, we return the number with
        the largest value?
    How do we figure out the distance to 0?
        We do this by taking the absolute value of the value at the array index.
    If we have multiple answers, how do we determine the larger value?
        We can do this by taking the max between the two values stored at the array 
        indicies originally stored.

# M-atch: 
    I don't think this really matches any common array or string patterns, we don't
    need a hash map, sliding window, sorting, or two pointers. I think we can solve
    this doing a single pass through the array.

# P-lan:
    1.) Create our variable(s)
        For our variable do we store the index or the value of the largest number???
    2.) Going through the array
    3.) Check if the absolute value of the index we're looking at is equal to our current
    4.) If so, set the largest value's index to the variable
    5.) Otherwise, check if the value is less than our current
    6.) If so, update our variable
    7.) Return our variable

# I-mplement:
"""

def findClosestNumber(nums: List[int]) -> int:
    # Create our variable to store the closest number
    closest = nums[0]

    # Iterating over the input array
    for i in range(1, len(nums)):
        # Check if the absolute value of our current closest is equal to the index
        if abs(nums[i]) == abs(closest):
            # Then we take the max of the values
            closest = max(closest, nums[i])
        # Otherwise, we'll check if the absolute value of the index is less than the current
        elif abs(nums[i]) < abs(closest):
            # Update the variable
            closest = nums[i]
    
    # Return the closest number to 0
    return closest


nums =  [-4, -2, 4, 8]           # Expects 1
nums2 = [2, -1, 1]                  # Expects 1, 1 > -1 so we return 1

print(findClosestNumber(nums))
print(findClosestNumber(nums2))




