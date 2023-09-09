# LC 90: Subsets II
# https://leetcode.com/problems/subsets-ii/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an integer array nums, that may contain duplicates.
    # ? What is our output ?
        Our output is all the possible subsets returned in a list.
    # ? Does the order in which we return the subsets matter ?
        No, the problem says that we can return the solution in any order.
    # ? Can we have duplicate subsets ?
        No, the problem states that we must not contain any duplicate subsets.
    # ? Can our input be empty ?
        No, the constraints state that the minimum length our input can be is 1
    to 10
    # ? What values can we have in our input ?
        The constraints state that the values in our input can range anywhere
    between -10 to 10.

M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointers
        2) Sorting
        3) Sliding Window
        4) Storing in a Hash Map or Set
    
        None of these common patterns can be used to solve this problem, and
    considering that it's the sequel to a problem we've already done, that
    being Subsets, we can probably use backtracking as well. This makes sense
    since we want to explore all combinations. 
        This is very similar to subets 1, but we gotta make sure that we don't
    explore the decision where the number is a duplciate. How do we do this?
    We can't gurantee that our array is sorted, so we can call that. We know
    that sorting takes O(nlog(n)) time but that is neglible in this problem
    since the runtime is going to be O(n * 2^n). n from the amount of elements
    in our input array, and 2^n from the number of combinations that can be
    generated.
        So we can create our result list, and sort our input array. We can then
    declare our helper function that takes in an index and a subset. From here,
    we can check for our base case, and that is the same as the previous subset
    problem, with the index out of bounds. If this is the case, we want to
    append a copy of the subset to the result list, and then return. 
        We can then explore the decision in which we choose to include
    nums[index]. Here we can append the value at the index to the subset, then
    recursively call the function with an incremented index and the same 
    subset. 
        Next, we can explore the decision in which we don't include
    nums[index] and we can begin by first popping the value we just appened
    and then check if the index is not out of bounds and if the current 
    value is the same as the value in the next index. If this is the case
    we know that we can increment the index. Once we've reached a distinct
    value, we can recursively call the function with an incremented index and
    the subset. 
        Outside, of the helper function, we can call it by passing in a 0
    and an empty list. Since the function appends to the result list, we can
    just return it after.

P-lan:
    1) Create our result list and sort nums
    2) Declare our dfs helper function that takes in an index and a subset
    3) Base Case: Check if the index is out of bounds
        i) If so, append a copy of the subset to the result list
        ii) Return
    4) Append nums[index] to the subset
    5) Recursively call the function with an incremented index
    6) Pop the value we just added
    7) Check if the index is not out of of bounds and that the next index has
       the same value as the current one.
        i) If so, increment the index
    8) Recursively call the function with an incremented index
    9) Outside the helper function, call it with a 0 and an empty list passed in
    10) Return the result list.

I-mplement:
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Create our result list
        result = []
        # Sort our input array
        nums.sort()

        # Define our backtracking helper function
        def backtrack(index, subset):
            # BASE CASE
            if index >= len(nums):
                result.append(subset[:])    
                return

            # Decision to include nums[i]
            subset.append(nums[index])
            backtrack(index + 1, subset)

            # Decision to not include nums[i]
            subset.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, subset)

        # Call our helper function
        backtrack(0, [])

        # Return result list
        return result


    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.subsetsWithDup(nums)}\n")


# Testing
test = Solution()

# Expects [[],[1],[1,2],[1,2,2],[2],[2,2]]
test.display(nums = [1,2,2])

# Expects [[],[0]]
test.display(nums = [0])