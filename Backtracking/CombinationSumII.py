# LC 40: Combination Sum II
# https://leetcode.com/problems/combination-sum-ii/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is a integer array, candidates, and a target number, target.
    # ? What is our output ?
        Our output is a list of all unique combinations in candidates, where
    the candidate numbers sum to target.
    # ? Can we reuse the same candidate ?
        No, the problem specifies that each number in candidates may only be
    only used once in the combination.
    # ? Can we have duplicate combinations ?
        No, the solution set must not contain duplicate combinations.
    # ? Are there any runtime or memory restrictions ?
        No, the problem doesn't specify any runtime or memory restrictions,
    but since we are generating every possible combinations, we know that the
    runtime of this algorithm will be O(2^n) since we have the choice between
    including a number or not, for n number of elements. 
    # ? Can our candidate list or target value be empty ?
        No, the minimum values that both the candidate length and the target
    can be is 1
    # ? Can we have negative values in our candidate list ?
        No, the values in our list range from 1 to 50.
    # ? Can there be duplicate numbers in our candidate list /
        Yes, there can be multiple instances of the same number.

M-atch:
        Considering that we are generating all possible combinations, as well
    as this being a sequel to a previous problem, Combination Sum I, we're
    going to have to implement a backtracking solution. Since we know that
    our runtime is going to be O(2^n), we can sort our candidate list so that
    we can have all the duplicate numbers next to each other. The reason for
    this is because we want to explore combinations that don't have duplicate
    numbers, because if we didn't we'd find that we'd be generating duplicate
    combinations. From there, we can create our result list and define our
    backtracking helper function. This function will take on the current 
    combination, an index, and the target. For this solution we'll be 
    subtracting the candidate values from the target until the target reaches
    0 or becomes less than 0, thus defining our base cases. 
        Our first base case will be when the target = 0, meaning that we found
    a valid combination, we'd append a copy of the combination to the result 
    list. The other case is when the target is less than 0, this means that
    we've subtracted too much and is considered an invalid input. In this case,
    we'd just return. 
        We can then start generating our combinations, but first we must define
    a previous variable to keep track of the value we just saw, we can 
    initialize this to -1, since we know from the constraints that candidates
    will never be a negative value. Then, iterating from the position variable
    to the end of the input array, we must first check if the current candidate
    is equal to the previous variable, on the first run this won't be true so
    it's fine. From here, we can then explore the combinations of where we 
    include the value. To do this, we must first append to the current
    combination the value we're looking at. We can then recursively call the 
    function with the same combination, an incremented index, and the target
    subtracted by the value of the candidate. 
        We can the explore the combinations where we use a new value, to do
    this, pop the element we just added and set previous to the value of the
    candidate, this makes sure that in the recursive call we explore 
    combinations that include a distinct number. Then, outside the function
    we can call it by passing in an empty list, a 0, and the target. Finally,
    we can just return the result list.


P-lan:
    1) Sort our candidate list
    2) Create our result list
    3) Define our backtracking function that takes in the current combination,
    an index, and the target
    4) Check the case where our target is equal to 0
        i) If this is the case, append a copy of the combination to the result list
        ii) Return
    5) Check the case where our target is less than 0
        i) If so, return
    6) Create a previous variable and set it to 0.
    7) Iterating over the length of the input array, starting at position
        i) Check if the current candidate is equal to the previous value
            a) If so, continue onto the next iteration
        ii) From there, we append the candidates value to the current combination
        iii) Recursively call the function with an incremented index
        iv) Pop the value we just added
        v) Set the previous variable to the candidate
    8) Call the backtracking function
    9) Return result


I-mplement:
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the input array
        candidates.sort()

        # Create our result list
        result = []

        # Define our backtracking function
        def backtrack(curr_combo, index, target):
            # Base Case: Check if target is equal to 0
            if target == 0:
                # Append a copy of the current combination to the result list
                result.append(curr_combo[:])
                return
            # Base Case: Check if the target is less than 0
            if target <= 0:
                return
            
            # Create our previous variable
            prev = -1
            # Iterating over the length of the array, starting at index
            for i in range(index, len(candidates)):
                # Check if the current candidate is the same as the previous
                if candidates[i] == prev:
                    # Continue onto the next iteration
                    continue

                # Append the value to the current combination list
                curr_combo.append(candidates[i])

                # Recursively call the function with updated parameters
                backtrack(curr_combo, i + 1, target - candidates[i])

                # Pop the value we just appended
                curr_combo.pop()

                # Update previous variable
                prev = candidates[i]
        
        # Call the backtracking function
        backtrack([], 0, target)
        # Return result list
        return result


    def display(self, candidates: List[int], target: int) -> None:
        print(f"Input: candidates = {candidates}, target = {target}")
        print(f"Output: {self.combinationSum2(candidates, target)}\n")


# Testing
test = Solution()

# Expects [[1,1,6],[1,2,5],[1,7],[2,6]]
test.display(candidates = [10,1,2,7,6,1,5], target = 8)

# Expects [[1,2,2,],[5]]
test.display(candidates = [2,5,2,1,2], target = 5)