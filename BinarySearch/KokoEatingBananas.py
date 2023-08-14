# LC 875: Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Yzer De Gula

from typing import List
import math

"""
U-nderstand:


M-atch:


P-lan:


I-mplement:
"""
# 107/125 test cases passed
class Solution:
    def minEatingSpeedBrute(self, piles: List[int], h: int) -> int:
        # Get max pile
        max_pile = max(piles)

        # Iterate from 1 to max pile
        for k in range(1, max_pile + 1):
            # Declare total time
            total_time = 0

            # Iterate through piles
            for pile in piles:
                # Add time to total time
                total_time += math.ceil(pile / k)
                # print(f"total_time: {total_time}")
            # If total time is less than or equal to h,
            if total_time <= h:
                # return k
                return k

        # If total time is greater than h, return max pile
        return max_pile

# The Time Compelxity of this solution is O(N * M) this is because the inner
# loop iterates through the piles and the outer loop iterates through the
# possible values of k. 
# The Space Complexity of this solution is O(1) because we are not using any
# additional space.


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Delcare our two pointers
        left, right = 1, max(piles)
        # Declare our result variable
        result = max(piles)

        # While our two pointers havent crossed
        while left <= right:
            # Calculate our mid (eating speed)
            k = (left + right) // 2

            # Declare our total time
            total_time = 0


            # Iterate through piles
            for pile in piles:
                # Add time to total time
                total_time += math.ceil(pile / k)


            # If total time is less than or equal to h,
            if total_time <= h:
                # Update our result
                result = min(result, k)
                # Update our right pointer
                right = k - 1
            # Otherwise,
            else:
                # Update our left pointer
                left = k + 1

        # Return our result
        return result
    
# The Time Complexity of this solution is O(N * log M) this is because the
# inner loop iterates through the piles and the outer loop iterates through
# the possible values of k. The outer loop is log M because we are using
# binary search.
# The Space Complexity of this solution is O(1) because we are not using any
# additional space.
    

    def display(self, piles: List[int], h: int) -> None:
        print(f"Input: piles = {piles}, h = {h}")
        print(f"Output: {self.minEatingSpeedBrute(piles, h)}")
        print(f"Output: {self.minEatingSpeed(piles, h)}\n")


# Testing
test = Solution()

# Expected: 4
test.display([3,6,7,11], 8)

# Expected: 30
test.display([30,11,23,4,20], 5)

# Expected: 23
test.display([30,11,23,4,20], 6)