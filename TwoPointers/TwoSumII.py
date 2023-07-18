# LC 167: Two Sum II - Input Array is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is a 1-indexed integer array named numbers
    - What is our output?
        Our output is a List of length 2 that holds the 2 indices that add up
        to the target value. So we would have to add 1 to the indices of our 
        result
    - Is it guranteed for a solution to exist?
        Yes, the problem states that the tests have exactly one solution, which
        means that we also don't have to worry about multiple solutions
    - Can the input array be empty? 
        No, the minimum length of the input array is 2
    - How is the array sorted?
        The array is sorted in non-decreasing order (increasing)
    
    Happy Case:
    Input: numbers = [1,2,4,7,9], target = 9
    Output: [2,4]
    Explanation: Since the array is 1-indexed, 2 and 7 were originally at indices
    1 and 3, adding one to both of them our result is now 2 and 4

    Input: numbers = [2,3,8,10], target = 5
    Output: [1,2]

M-atch:
    For array and string questions, common patterns for solutions include:
        1) Two Pointers
        2) Sorting
        3) Storing in a Hash Map or Set
        4) Sliding Window
    
    Sorting wouldn't help because our input array is already sorted. Sliding window
    wouldn't help either. Hash Map can be used like in Two Sum I, but we can take 
    advantage of the fact that our input array is sorted and use Two Pointers. We
    have a left and right pointer, the left one is at the beginning of the input
    array, and the right pointer is at the end of the array. Then, while our two
    pointers haven't crossed we can declare a var to track the current sum. In the
    case the current sum is greater than the target, we know that we must decrement
    our right pointer. In the case that the sum is less than the target, we can 
    increment the left pointer. Then the final case would be that the sum is equal
    to the target. We can then return the indices plus 1 in that last case. 

P-lan:
    1) Declare our left and right pointers
    2) While our two pointers haven't crossed
    3) Declare a var to track the current sum
    4) If the sum is greater than the target, decrement the right pointer
    5) If the sum is less than the target, increment the left pointer
    6) Otherwise, our sum is equal to the tagert, return the indices plus 1
    7) Even though it's not neccessary, we can return an empty list

I-mplement:
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Declare our left and right pointers
        left, right = 0, len(numbers) - 1

        # While our two pointers haven't crossed
        while left < right:
            # Declare our current sum
            current_sum = 0

            # If the current sum is greater than the target
            if numbers[left] + numbers[right] > target:
                # Decrement right pointer
                right -= 1
            
            # If the current sum is less than the target
            elif numbers[left] + numbers[right] < target:
                # Increment left pointer
                left += 1
            
            # Otherwise, the current sum is equal to the target
            else:
                # Return the indices plus one
                return [left + 1, right + 1]
        
        # Not neccessary, but return empty list if a solution doesn't exist
        return []
    

# Testing
solution = Solution()

# Expects [1,2]
nums1, target1 = [2,7,11,15], 9
print("Input Array: ", nums1)
print("Target:      ", target1 )
print("Output:      ", solution.twoSum(nums1,target1))

print("\n")

# Expects [1,3]
nums2, target2 = [2,3,4], 6
print("Input Array: ", nums2)
print("Target:      ", target2 )
print("Output:      ", solution.twoSum(nums2,target2))

print("\n")

# Expects [1,2]
nums3, target3 = [-1,0], -1
print("Input Array: ", nums3)
print("Target:      ", target3 )
print("Output:      ", solution.twoSum(nums3,target3))
