# LC 15: 3Sum
# https://leetcode.com/problems/3sum/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an integer array, nums.
    - What is our output?
        Our output is a triplet [nums[i], nums[j], nums[k]] such that they're
        distinct indices from our array and add up to 0.
    - Can the input array be empty?
        No, the constraints state that the minimum number of elements in our
        input array is 3.
    - Is there guranteed for a solution to exist?
        No, in one of the test cases, the only possible triplet doesn't add sum
        up to 0.
    - Can there be multiple solutions?
        Yes, in one of the test cases, the output has two different triplets. 
        This means that we are looking for a solution set and not just a single
        possible solution. 
    - Is our input array sorted?
        No, our input array is not sorted.


    Happy Case:
    Input: nums = [-3,0,1,2]
    Output: [[-3,1,2]]

    Input: nums = [-4,-2,-1,0,3,4]
    Output: [[-4,0,4], [-2,-1,3]]

    Edge Case:
    Input: nums = [3,2,1]
    Output: []

M-atch:
    For arrays and strings, common patterns for solutions include:
        1) Sorting
        2) Two Pointers
        3) Sliding Window
        4) Storing in Hash Map or Set
    
    Sliding window won't help find a solution, I think if we stored it in a 
    Hash Map or Set it could work, but wouldn't be efficient. For this problem,
    I think we can first sort the array, and use two pointers like we did in
    Two Sum II. We can first declare our result list in the case a solution
    doesn't exist. Then we'd sort our array, and then have a for loop that
    is enumerated over nums so we can keep track of the index and value. We
    then check if the index is greater than 0 and that it's not the same
    value as the previous index, this make sure we don't compute the same
    sum. In this case we'd continue onto the next iteration. From there,
    we can calculate our left and right pointers. The left one should
    be declared as one more than the current index since the current
    index acts as the a, for a + b + c = 0. The right one should be
    the end of the nums array len(nums) - 1. Then on, this should just be Two
    Sum II and while our two pointer haven't crossed, declare our current sum
    var to be equal to a + nums[left] + nums[right]. We check if the sum is 
    greater than 0 and if so, decrement our right pointer. If the sum is less
    than 0, increment our left pointer. Otherwise, our sum is equal to zero
    and we'd append the triple to our result list, and increment our left pointer
    to check if there are any more solutions for this current iteration. But
    we need to keep in mind if this increment is distinct from the previous 
    value and that our two pointer's haven't crossed, and keep incrementing
    our left pointer until we come across a distinct value or our pointers 
    crossed. Finally, return our solution set.


P-lan:
    1) Declare our result list
    2) Sort our input array
    3) Iterating over enumearted input array
    4) Check if the current index is greater than 0 and that it's a distinct
       value from index 0
    5) Declare our left and right pointers
    6) While our pointers haven't crossed
    7) Declare our current sum being the value of the current index, nums[left]
       and nums[right]
    8) Check if our sum is greater than 0, if so decrement right pointer
    9) Check if our sum is less than 0, if so increment left pointer
    10) Otherwise, our sum is equal to 0, and we'd append that triple to the
        result list
    11) Increment our left pointer to check if there's any other triples
    12) Check if that increement is distinct from the previous value and 
        that our pointers haven't crossed
    13) Return result list


I-mplement:
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Declare our result list
        result = []

        # Sort our input array
        nums.sort()

        # Iterating over our input array enumerated
        for i, a in enumerate(nums):
            # Check if current index is greater than 0 and that it's a distinct
            # value from the previous index
            if i > 0 and a == nums[i - 1]:
                # Continue onto the next iteration
                continue

            # Calculate our left and right pointers
            left, right = i + 1, len(nums) - 1

            # While our pointers haven't crossed
            while left < right:
                # Declare our current sum
                current_sum = a + nums[left] + nums[right]

                # If our sum is greater than 0
                if current_sum > 0:
                    # Decrement right pointer
                    right -= 1
                
                # If our sum is less than 0
                elif current_sum < 0:
                    # Increment left pointer
                    left += 1
                
                # Otherwise, our sum is equal to 0
                else:
                    # Append that triple to our result list
                    result.append([a, nums[left], nums[right]])

                    # Increment our left pointer to check for any other
                    # possible triples
                    left += 1

                    # Check if the increment is distinct and our pointers haven't crossed
                    while nums[left] == nums[left - 1] and left < right:
                        # Increment our left pointer
                        left += 1
        
        # Return our result list
        return result


# Testing 
solution = Solution()

# Expects []
nums1 = []
print("Input:  ", nums1)
print("Output: ", solution.threeSum(nums1))

print("\n")

# Expects [[-1,-1,2], [-1,0,1]]
nums2 = [-1,0,1,2,-1,-4]
print("Input:  ", nums2)
print("Output: ", solution.threeSum(nums2))

print("\n")

# Expects []
nums3 = [0,1,1]
print("Input:  ", nums3)
print("Output: ", solution.threeSum(nums3))

print("\n")

# Expects [[-3,1,2]]
nums4 = [2,-3,0,1]
print("Input:  ", nums4)
print("Output: ", solution.threeSum(nums4))

print("\n")

# Expects [[-4,0,4], [-2,-1,3]]
nums5 = [4,3,-4,-2,-1,0]
print("Input:  ", nums5)
print("Output: ", solution.threeSum(nums5))