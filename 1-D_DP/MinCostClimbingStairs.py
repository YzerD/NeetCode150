# LC 746: Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an integer array called, cost. Where cost[i] represents
    the cost that step takes. Once you pay that cost you can climb either
    one or two steps. We can also start from step 0 or step 1
    # ? What is our output ?
        Our output is the minimum cost to reach the top of the floor
    # ? What is the top of the floor ?
        The top of the floor is one past the end of the array. Take the first
    example on LeetCode, the answer is 15 because we can start at step 1, pay
    the cost, and climb 2 steps to get to the end of the array.

M-atch:
    Since Dynamic Programming is entirely new to me, I watched the Video 
Solution of this problem. To phrase Dynamic Programming in my own words
it's a way to skip over recalculating sub-problems like we have done in
a recursive solution. So for this problem, we can append a 0 to act as
the top of the floor. We can then iterate backwards through the input
array but starting at the third to last element, leaving two elements
at the end available. We can then calculate the min cost from taking
a single step or a double step. We can then return the min of the first
or second element since that's the min cost of the entire path.

P-lan:
    1) Append a 0 to the end of the input array
    2) Starting at the third to last element, iterate backwards
    3) Caclulate the min cost path of a single step or a double step
       at the current step
    4) Return the min cost of the first or second element


I-mplement:
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Append 0 to input array
        cost.append(0)

        # Starting at the third element, iterate backwards
        for i in range(len(cost) - 3, -1, -1):
            # Calculate the min cost of a single or double step for the current step
            cost[i] += min(cost[i + 1], cost[i + 2])

        # Return the minimum value between the first or second element.
        return min(cost[0], cost[1])

    
    def display(self, cost: List[int]) -> None:
        print(f"Input: cost = {cost}")
        print(f"Output:       {self.minCostClimbingStairs(cost)}")


# Testing
sol = Solution()

# Expects 15
cost = [10,15,20]
sol.display(cost)

# Expects 6
cost = [1,100,1,1,1,100,1,1,100,1]
sol.display(cost)