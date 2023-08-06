# LC 42: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is a non-negative integer array representing an eleveation map
        where the width of each bar is 1
    # ? What is our output ?
        Our output is how much water the elevation map can trap after raining
    # ? What determines trapped water ?
        Trapped water is the amount of space that can be held between an index's
        adjacent heights. The amount of water is bottle-necked by the lesser 
        height of the adjacent bars, this is because if we were to add more water
        the lesser value limits it. 
    # ? Can our input array be empty ?
        No, the constraints state that the minimum length that our input array
        can be is 1
    # ? Can we negative values in our input array ?
        No, the constraints state that the minimum value an element can be in our
        input array is 0. 

M-atch:
    For arrays and strings, common patterns for solutions are:
        1) Two Pointers
        2) Sliding Window
        3) Storing in a Hash Map or Hash Set
        4) Sorting
    
    For this problem, Sorting would mess up the order of the input array which is
    important since it would alter where the trapped rain is. Hash Map, Hash Set,
    and Sliding Window aren't useful for this case as well. This would leave two
    pointers, which makes sense since this is very similar to another problem,
    Container with most water. For this problem we can have additional variables,
    left max and right max. These are gonna be used for storing the max height
    we've encoutnered so far. So while our two pointers haven't crossed, if the
    left max is less than the right max, we know that there might be trapped 
    water at the left pointer's position. So we can increment the pointer and
    take the max of the current max and the value held at the left pointer. We
    do this since, we know that the left max is the limiting factor of the water,
    since it's less than the right. We use the max on the left max and left pointer
    to make sure we calculate the most potentially trapped water. The reason for 
    the increment is that it serves as the right barrier of the index we're currently
    checking. Knowing that, we can calculate the amount of trapped water by adding
    the difference of the left max and the value held at that position. The same logic
    applie to the right pointer as well. 
    

P-lan:
    1) Declare our left and right pointers
    2) Declare our left and right max variables
    3) Declare our result variable
    4) While our two pointers haven't crossed
    5) if left max is less than right 
    6) Increment our left pointer
    7) Take the max of the left max and the value held at left pointer
    8) Append the difference of the left max and the value held at the left pointer
    9) Otherwise, the left pointer is greater than or equal to the right
    10) Decrement the right pointer
    11) Take the max of the right max and the value held at the right pointer
    12) Append the difference of the right max and the value held at the right pointer
    13) Return the result

I-mplement:
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # Declare our left and right pointers
        left, right = 0, len(height) - 1

        # Declare our left and right maxes
        left_max, right_max = height[left], height[right]

        # Declare our result variable
        result = 0

        # While our two pointers haven't crossed
        while left < right:
            # If the left max is less than the right max
            if left_max < right_max:
                # Increment the left pointer
                left += 1
                # Get the max of the current max and the value held at the left pointer
                left_max = max(left_max, height[left])
                # Append the difference of the max and the value held at the left pointer
                result += left_max - height[left]

            # Otherwise, the left max is greater than or equal to the right max
            else:
                # Decrement the right pointer
                right -= 1
                # Get the max of the current max and the value held at the right pointer
                right_max = max(right_max, height[right])
                # Append the difference of the max and the value held at the right pointer
                result += right_max - height[right]

        # Return result 
        return result


    def display(self, height: List[int]) -> None:
        print(f"Input:  {height}")
        print(f"Output: {self.trap(height)}\n")


# Testing
solution = Solution()


# Expects 6
height = [0,1,0,2,1,0,1,3,2,1,2,1]
solution.display(height)

# Expects 9
height = [4,2,0,3,2,5]
solution.display(height)