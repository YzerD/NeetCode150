# LC 875: Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/
# Yzer De Gula

from typing import List
import math

"""
U-nderstand:
    # ? What is our input ?
        Our input is a list of piles of bananas and an integer h which is the
    number of hours Koko has to eat all the bananas.
    # ? What is our output ?
        Our output is an integer which is the minimum integer Koko can eat per
    hour to finish all the bananas within h hours.
    # ? Do we have constraints ?
        1 <= piles.length <= 10^4
        piles.length <= h <= 10^9
        1 <= piles[i] <= 10^9
    # ? Can our input be empty ?
        No, our input cannot be empty. The constraints state that piles.length
    is at least 1.
    
M-atch:
        For this problem we can initially started off by using a brute force 
    approach. We can iterate through the piles and for each pile we can
    calculate the time it takes to eat the pile. We can then add the time to
    a total time variable. If the total time is less than or equal to h, we
    can return the current value of k. If the total time is greater than h,
    we can return the max pile. This solution will work but it will be slow.

        We can optimize this solution by using binary search. We can declare two
    pointers, left and right. Left will be 1 and right will be the max pile.
    We can then calculate the mid (eating speed) by adding left and right and
    dividing by 2. We can then iterate through the piles and calculate the
    total time it takes to eat all the piles. If the total time is less than
    or equal to h, we can update our result to be the minimum of our current
    result and k. We can then update our right pointer to be k - 1. If the
    total time is greater than h, we can update our left pointer to be k + 1.
    We can continue this process until our left pointer is greater than our
    right pointer. We can then return our result.


P-lan:
    Brute Force:
    1) Get max pile
    2) Iterate from 1 to max pile
    3) Declare total time
    4) Iterate through piles
    5) Add time to total time
    6) If total time is less than or equal to h,
    7) return k
    8) If total time is greater than h, return max pile

    Binary Search:
    1) Delcare our two pointers
    2) Declare our result variable
    3) While our two pointers havent crossed
    4) Calculate our mid (eating speed)
    5) Declare our total time
    6) Iterate through piles
    7) Add time to total time
    8) If total time is less than or equal to h,
    9) Take the min of our result and k
    10) Update our right pointer
    11) Otherwise, we know that k is too small
    12) Update our left pointer
    13) Return our result

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