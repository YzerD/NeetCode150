# LC 78: Subsets
# https://leetcode.com/problems/subsets/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an integer array nums of unique elements
    # ? What is our output ?
        Our output is all possible subsets of our input in a list
    # ? What is a subset ?
        A subset of an array is a selection of elements (possibly none)
    of the array.
    # ? Can our input array be empty ?
        No, the constraints of the problem states that the minimum length that our
    input array can be is 1
    # ? Can we have duplicate values in our input array ?
        No, the constraints of the problem states that every number in our 
    input array is unique
    # ? What values can the elements in our input array have ?
        The constraints state that the possible values that our elements in our
    input array can take is -10 to 10.
    # ? Are duplicate subsets allowed ?
        No, The problem specifies that the solution set must not contain
    duplicate subsets.

M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointers
        2) Hash Map or Hash Set
        3) Sorting
        4) Sliding Window
    
        For this problem, none of the common patterns are applicable for this
    problem. This is because for subsets there are 2^n different possible
    subsets. Since we want the actual subsets rather than the number of subsets
    the most efficient our algorithm can be is O(n * 2^n). We can use 
    backtracking which is the brute force as well as the most efficient
    solution for this problem.
        Backtracking is a general algorithm for finding (or some) solutions to
    some computational problems. For this problem we can go through our input
    array and we can explore the path of where we either add the element or 
    don't. 
        So for our solution we can first create our variables this being a 
    result variable and a subsets variable. We can then declare our helper
    function which would could be considered a dfs approach since we want
    to explore as far down our possible subset combinations. The parameter
    of our helper function can be the current index we are looking at, since
    we want to see the possible combinations of whether we add it or don't.
        So the first condition or base case we need to check for is if the
    index is out of bounds, this can be done by i >= len(nums). If it isn't
    then we can proceed with our backtracking algorithm. We can first append
    to the result list a copy of our subsets list via the copy function. We
    can then first get the path where we do add the element. This can be done
    by appending the value held by the index to the subsets list, and then
    recursively calling the helper function. Then we must explore the case
    where we don't add the element. We can pop from the subsets list and then
    recursively call the helper function with the index plus 1.
        Then ouside of our function we can call the helper function with the
    first index of our input array passed in, this being 0. We can then return
    the result list.
    
P-lan:
    1) Create our result and subsets list
    2) Declare our dfs helper function
    3) Check if our index is out of bounds
    4) We can then append a shallow copy of our subsets list to the result list
       using the copy() function
    5) We can then explore the path where we do add the element
        i) Add the value held at the index to the subsets list
        ii) Recursively call the function with the index plus 1
    6) We can then explore the path where we do not add the element
        i) Pop the element we just added from the list
        ii) Recursively call the function with the index plus 1
    7) Outside the helper function we can call it with a 0 passed in
    8) We can then return the result list


I-mplement:
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Create our result and subsets list
        result, subsets = [], []

        # Declare our dfs helper function that takes in an index as a parameter
        def dfs(i):
            # Check if the index is out of bounds
            if i >= len(nums):
                # Append to the result list a copy of the subsets
                return result.append(subsets.copy())
            
            # Otherwise, we can explore the decision where we add the element
            subsets.append(nums[i])
            dfs(i + 1)

            # We can then check the decision where we do not add the element
            subsets.pop()
            dfs(i + 1)
        
        # We can call the helper function
        dfs(0)

        # Return the result list
        return result
    

    def display(self, nums: List[int]) -> None:
        print(f"Input: nums = {nums}")
        print(f"Output: {self.subsets(nums)}\n")


# Testing
test = Solution()

# Expects [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
nums = [1,2,3]
test.display(nums)

# Expects [[],[0]]
nums = [0]
test.display(nums)