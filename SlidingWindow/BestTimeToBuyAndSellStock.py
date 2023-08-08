# LC 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Resources Used: https://www.geeksforgeeks.org/window-sliding-technique/#
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array called prices, where prices[i] is the price of a
    given stock on the ith day
    # ? What is our output ?
        Our output is the maxmimum profit you can achieve from this
    transaction, if you cannot achieve any profit, return 0.
    # ? How is maximum profit determined ?
        Maximum profit is determined by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock. 
    # ? Can our input array be empty ?
        No, the constraints of the problem state that the minimum length the 
    input array can be is 1

M-atch:
    For Arrays and Strings, common patterns for problems include:
        1) Sorting
        2) Two Pointers
        3) Sliding Window
        4) Storing Elements in Hash Map or Hash Set

        I don't think sorting or Hash Map / Set would help solve this problem,
    since it would alter the order of the input array and we need that so we
    can calculate the max profit of a future day from the buying point. So we
    can either use Two Pointers or Sliding Window. I think for Two Pointers
    we can declare our left pointer at the very first element and the right
    pointer to the next element. While our left pointer is less than the right
    calculate the current profit of the right minus the left pointer. Then we
    can get the max of the currently held max profit to the current profit.
    Otherwise, we know that we've encounter a lower point and so we'd set
    left to the right and increment the right. We can then reutrn the max profit.


P-lan:
    Plan 1 (Two Pointers):
        1) Declare our left and right pointers
        2) Declare our max profit vairable
        3) While our right pointer hasn't reached the end of the input array
        4) Check if the left pointer is less than the right
        5) If so, calculate the current profit
        6) Then take the max of the current max profit and the current profit
        7) Otherwise, we know that right has a lesser value than our left
        8) Set left to right
        9) Increment right pointer
        10) Return max profit


I-mplement:
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Declare our two pointers
        left, right = 0, 1
        
        # Declare our max profit
        max_profit = 0

        # While our right pointer hasn't reached the end of the array
        while right < len(prices):
            # If our left pointer value is less than the right
            if prices[left] < prices[right]:
                # Calculate the current profit
                current_profit = prices[right] - prices[left]
                # Take the max of the current max profit and the current profit
                max_profit = max(max_profit, current_profit)
            # Otherwise, we know that right has a lesser value than left
            else:
                # So we can set our left to our right
                left = right
            # Increment our right pointer
            right += 1
        
        # Return max profit
        return max_profit

# From NeetCode
    def maxProfitSliding(self, prices: List[int]) -> int:
        # Declare a variable to hold our max profit
        res = 0
        
        # Declare a variable set at the first element to act as our lowest price
        lowest = prices[0]

        # For each price in our array
        for price in prices:
            # If the price is lower than our currently held lowest
            if price < lowest:
                # Set the lowest to that value
                lowest = price
            # Otherwise, take the max of our currently held max profit to the current
            res = max(res, price - lowest)
        # Return max profit
        return res


    def display(self, prices: List[int]) -> None:
        print(f"Input: prices = {prices}")
        print(f"Output:         {self.maxProfit(prices)}\n")


# Testing
sol = Solution()

# Expects 5
prices = [7,1,5,3,6,4]
sol.display(prices)

# Expects 0
prices = [7,6,4,3,1]
sol.display(prices)