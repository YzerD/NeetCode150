# LC 1046: Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/
# Yzer De Gula

from typing import List
import heapq

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array that represents the weight of stones
    # ? What is our output ?
        Our output is the last element or weight of the last stone
    # ? Can there not be a last stone ?
        Yes, if there are no stones left, return 0
    # ? What happens when we take the two heaviest stones ?
        If they are equal, both are destroyed, if x != y, x is destroyed and
    y is now y - x.


M-atch:
        I think for this problem we can use a heap, specifically a max heap so
    that we can get the heaviest stone easily. Another option I think we can do
    is sort the array, and check the logic for the last stone and the second to
    last stone. Pop whenever the two are equal to eachother, and then if
    x != y, pop the last elements and insert x - y. However, we should first
    check for the cases when the length of the stones array is 0 or 1. 
        
P-lan:
    1) Check if the length of the array is 0, if so, return 0
    2) While the array is greater than 1 (Since we want the last stone)
    3) Sort the array
    4) Declare our two stones to check, the last and second to last
    5) If they're equal, pop both from list
    6) If x != y, pop both from list and insert x - y
    7) Check if the length of the array is 1, if so, return stones[0]
    8) After doing this, we should return 0, since there wouldn't be an element left


I-mplement:
"""

class Solution:
    def lastStoneWeightNaive(self, stones: List[int]) -> int:
                # If the length of the array is 0
        if len(stones) == 0:
            # Return 0
            return 0

        # While there is more than 1 element in our array
        while len(stones) > 1:
            # Sort the array
            stones.sort()
            # Declare variables for the last and second to last stone
            stone_1, stone_2 = stones[-1], stones[-2]

            # In the case that x == y
            if (stone_1 == stone_2):
                # Pop both from list
                stones.pop()
                stones.pop()
            # Otherwise, x != y
            else:
                # Set stones_1 to y - x
                stone_1 = abs(stone_1 - stone_2)
                # Pop last elements
                stones.pop()
                stones.pop()
                # Append y - x
                stones.append(stone_1)

        # After all the computations, if there is one element left,
        if len(stones) == 1:
            # Return it
            return stones[0]
        
        # Otherwise, return 0
        return 0
    

    def lastStoneWeightOptimal(self, stones: List[int]) -> int:
        # Put stones in max heap using list comprehension
        stones = [-s for s in stones]
        # Heapify stones
        heapq.heapify(stones)

        # While there is more than one stone
        while len(stones) > 1:
            # Get the first stone 
            first = heapq.heappop(stones)
            # Get the second stone
            second = heapq.heappop(stones)

            # If the first stone is greater than the second stone
            if second > first:
                # Push the difference of the two stones
                heapq.heappush(stones, first - second)

        # If there is one stone left, return it       
        stones.append(0)
        return abs(stones[0])


    def display(self, stones: List[int]) -> None:
        print(f"Input: stones = {stones}")
        print(f"Output: {self.lastStoneWeightNaive(stones)}")
        print(f"        {self.lastStoneWeightOptimal(stones)}\n")


# Testing
test = Solution()

# Expects 1
test.display(stones = [2, 7, 4, 1, 8, 1])

# Expects 1
test.display(stones = [1])