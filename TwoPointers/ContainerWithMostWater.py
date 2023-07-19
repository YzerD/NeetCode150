# LC 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
            Our input is an array of integers that represent possible endpoints for
        our container
    - What is our output?
            Our output is the maximum area that we can form with the values from the
        input array.
    - How can we calculate the area?
            We know that the shape of the container is a rectangle, and therefore the
        area formula is length x width.
            The Width of the container is the minimum value of the endpoints, which
        in this case is min(height[index 1], height[index 2]). This is because
        the lesser value is the bottle neck of the container
            The length of the container is the furthest endpoint minus the other
        endpoint. This being (index 2 - index 1)
    - Can the input array be empty? 
        No, the constraints state that the minimum value we can have in the input
        array is 2.
    - Can there be any negative heights in the input array?
        No, only 0 and above are present in the array
    - Is the array sorted?
        No, the input array is not sorted

    Happy Case:
    Input: height = [2,3,4]
    Output: 4

    Edge Case:
    Input: height = [0,0]
    Output: 0


M-atch:
    For strings and arrays, common patterns for solutions include:
        1) Two Pointers
        2) Sorting
        3) Sliding Window
        4) Storing in a Hash Map or Set
    
    A naive solution is to use a nested loop to check every possible
    area for the current iteration and take the max of current max area
    and that of the current area. 

    Sorting wouldn't help since that would alter the output. Storing in
    a Hash Map or a set would complicate things, and a sliding window is
    not gonna help find a solution. So we can use two pointers. We can 
    declare our area and then our two pointers left and right. Left being
    at the beginning of the input array, right being at the end of the array.
    While our two pointers haven't crossed calculate the area and take the
    max of it. Then if the left value is less than that of the right pointer
    increment the left pointer. Otherwise, the right is less than or equal
    to the left, and we can decrement that. Finally, we can return our 
    max area.

P-lan:
    Plan 1 (Nested Loop):
        1) Declare our max area
        2) Itearting over the length of the entire array
        3) Iterating over the next index to the end of the array
        4) Calculate the area
        5) Take the max of the current max area and the current area
        6) Return the max area

    Plan 2 (Two Pointer):
        1) Declare our max area
        2) Declare our two pointers
        3) While our two pointers haven't crossed
        4) Calculate the area
        5) Take the max of the current max area and the current area
        6) If the left value is less than the right value
        7) Increment the left pointer
        8) Otherwise, decrement the right pointer
        9) Return the max area


I-mplement:
"""

class Solution:
    def maxAreaBrute(self, height: List[int]) -> int:
        # Declare our max area
        max_area = 0

        # Iterating over the entire array
        for i in range(len(height)):
            # Iterating over the next index to the end of the array
            for j in range(i + 1, len(height)):
                # Calculate the area
                curr_area = (j - i) * min(height[i], height[j])

                # Take the max of the max area and current area
                max_area = max(max_area, curr_area)
        
        # Return max area
        return max_area


    def maxAreaOptimal(self, height: List[int]) -> int:
        # Declare our max area
        max_area = 0

        # Declare our two pointers
        left, right = 0, len(height) - 1

        # While our pointers haven't crossed
        while left < right:
            # Calculate the area
            curr_area = (right - left) * min(height[left], height[right])

            # Take the max of the current max area and the current area
            max_area = max(max_area, curr_area)

            # Check if the left height is less than the right
            if height[left] < height[right]:
                # Increment left pointer
                left += 1
            # Otherwise, the right pointer is less than or equal to the left pointer
            else:
                # Decrement right pointer
                right -= 1
        
        # Return max area
        return max_area



# Testing
solution = Solution()


# Expects 49
# Got 48? Needed to take the min of the heights, since the lesser one bottle necks the area
height = [1,8,6,2,5,4,8,3,7]
print("Input:       ", height)
print("Brute Force: ", solution.maxAreaBrute(height))
print("Optimal:     ", solution.maxAreaOptimal(height), "\n") 


# Expects 1
height = [1,1]
print("Input:       ", height)
print("Brute Force: ", solution.maxAreaBrute(height))
print("Optimal:     ", solution.maxAreaOptimal(height))


"""
R-eview:
    - When testing the brute force method, I got 48 instead of 49. I first thought it was how
      the inner loop was declared. But then I forgot we need to take the min of the two heights
      to see which one bottle necks the area. This is because the lesser value determines the
      max water level the container can hold.

E-valuate:
    - Brute Force time complexity is O(n^2) and space should be O(1) since we aren't using any
      additional data structure
    - Optimal Solution's time complexity is O(n) since we only do one pass of all the elements
      in the worst case scenario. Space should be O(1) since we only use two pointers.
"""