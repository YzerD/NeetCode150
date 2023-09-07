# LC 39: Combination Sum
# https://leetcode.com/problems/combination-sum/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array of distinct integers, candidates and a target
    integer target.
    # ? What is our output ?
        Our output is a list of all unique combinations of candidates where the
    chosen numbers sum to target.
    # ? Does the order of which we return the combinations important ?
        No, the problem tells us that we can return the combinations in any
    order.
    # ? Can we repeat the same number in our combinations ?
        Yes, the same number can be repeated an unlimited number of times
    # ? What does it mean for a combination to be unique ?
        Two combinations are unique if the frequency of at least one of the 
    chosen numbers is different.
    # ? Can our input array be empty ?
        No, the minimum length our input array can be is 1
    # ? What values can be candidates ?
        The values in our input array can range from 2 to 40.
    # ? Can our target value be negative ?
        Our target value can range from 1 to 40

M-atch:
        This problem seems very similar to a previous one, that being Subsets.
    So, I think for this problem we can also implement a solution using a 
    backtracking algorithm. Thinking about the choices we can make for possible
    combinations, we can first see the combination where we add the first
    element, and then the next one would be the one where we don't. As with
    Subsets, we can have a dfs helper function to explore the different
    combinations, where we keep track of the position in the array we're at. 
    But for this problem I think it's important to keep track of the current
    value, and the total of the combination. This means that the base cases
    we need to look out for, is when the total is equal to the target, where
    we would then append the copy of the current combination to the result list.
    The other base case is to look for when the combination is invalid. This 
    could be either when the counter is out of bounds, or if the total is
    greater than the target. Where would then return out of the function. 


P-lan:
    1) Create our result list
    2) Declare our dfs helper function that takes in the current index, current
       combination, and the total.
    3) Check if the total is equal to the target
        i) If so, append to the result the copy of the current combination
        ii) Return
    4) Check if the counter is out of bounds or if the total is greater than
       the target.
        i) If so, return
    5) We can first explore the decision to add the element
        i) Recursively call the function with the same tracker and current
           combination, and update the total
    6) We can then explore the decision to add another element
        i) Pop from the current combination
        ii) Recursively call the function with an incremented counter, same
            combination and same total
    7) Outside the dfs helper, call the function with 0, an empty list, and
       another 0
    8) Since the dfs helper changes the result list, we can just return the 
       result list.

I-mplement:
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Create our result list
        result = []

        # Declare our dfs helper function
        def dfs(index, curr_combo, total):
            # Check if our total is equal to the target
            if total == target:
                # Append to the result list a copy of the current combination
                result.append(curr_combo.copy())
                return
            
            # Check if the index is out of bounds or if the total is greater than the target
            if index >= len(candidates) or total > target:
                return
            
            # Explore the option where we add the same value
            curr_combo.append(candidates[index])
            dfs(index, curr_combo, total + candidates[index])

            # Explore the option where we don't add the same value
            curr_combo.pop()
            dfs(index + 1, curr_combo, total)

        # Call the function outside the helper
        dfs(0, [], 0)   

        # Return the result list
        return result 


    def display(self, candidates: List[int], target: int) -> None:
        print(f"Input: candidates = {candidates}, target = {target}")
        print(f"Output: {self.combinationSum(candidates, target)}\n")


# Testing
test = Solution()

# Expects [[2,2,3],[7]]
test.display(candidates = [2,3,6,7], target = 7)

# Expects [[2,2,2,2], [2,3,3], [3,5]]
test.display(candidates = [2,3,5], target = 8)

# Expects []
test.display(candidates = [2], target = 1)