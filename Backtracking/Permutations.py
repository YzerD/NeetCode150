# LC 46: Permutations
# https://leetcode.com/problems/permutations/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array nums of distinct integers
    # ? What is our output ?
        Our output is a list of all the possible permutations
    # ? Does the order matter in which we return the permutations ?
        No, we can return the answer in any order.
    # ? What are permutations ?
        Permutations are a way in which a set or number of things can be
    ordered or arranged.
    # ? Can there be duplicates in our input array ?
        No, the problem tells us that all the integers in our input array
    are distinct.
    # ? Can our input array be empty ?
        No, the problem specifies that our input array can range from 1 to 6.

        
M-atch:
        Since we're trying to find all the different permutations in an integer
    array we can do backtracking, in order to explore all possible paths. This
    doesn't adhere to common patterns for strings and array problems. We can
    try to break down the problem recursively, with our base case being when
    there is only one element, because there is only one permutations for a
    single value. From there we can iterate through the input array, and then
    pop the first index, where we would then call the function recursively
    to break down the problem. Once we have, we would have to go back up and
    create the permutations, we would then iterate through the permutations and
    append the value we just popped back. Then we can add the permutation to 
    the result list and then append the number we popped from the input array
    back. We can then return the function.


P-lan:
    1) Create our result list
    2) Check if the length of nums is equal to 1
        i) If so, we've reached our base case and we'd return a copy of the
        nums list
    3) Iterating over the length of the input array
        i) Pop the first element in our input array
        ii) Recursively call the function 
    4) For each permutations, append the value we removed at the end
    5) Append the permutation to the result list
    6) Append the value we popped back into the input array
    7) Return the result 


I-mplement:
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Create our result list
        result = []

        # BASE CASE: Check if the length of nums is 1
        if len(nums) == 1:
            # return a copy of the list
            return [nums[:]]
        
        # Iterating over the input array
        for i in range(len(nums)):
            # Pop the first element
            val = nums.pop(0)
            # Recursively call the function
            perms = self.permute(nums)

            # Iterating over the permutations
            for perm in perms:
                # Append the value we removed at the end
                perm.append(val)

            # Append the permutation to the result list
            result.extend(perms)

            # Append the value we removed back into the input array
            nums.append(val)

        # Return the result list
        return result


    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.permute(nums)}\n")


# Testing
test = Solution()

# Expects [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
test.display(nums = [1,2,3])

# Expects [[0,1],[1,0]]
test.display(nums = [0,1])

# Expects [[1]]
test.display(nums = [1])