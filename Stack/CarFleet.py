# LC 853: Car Fleet
# https://leetcode.com/problems/car-fleet/
# Resources Used: https://www.w3schools.com/python/ref_func_zip.asp
# https://www.w3schools.com/python/python_lists_comprehension.asp
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is n cars going to the same destination that is represented
        by the parameter, target. We are also given two integer arrays position
        and speed, both of length n. Where position[i] is the position of the
        ith car and speed[i] is the speed of the ith car
    # ? What is our output ?
        Our output is the number of car fleets that will arrive at the 
        destination.
    # ? What is a car fleet ?
        A car fleet is some non-empty set of cars driving at the same position
        and same speed. Note that a single car is also a car fleet.
    # ? Can any cars start at the same position ?
        No, the constraints state that the values of the positions are unique.
    # ? Can our target or input arrays be empty ?
        Our target can be 0 but not negative, and the minimum our input arrays
        can be are 0
    # ? Can our input arrays be of differing lengths ?
        No, the number of cars n, is the same length as the length of the 
        position array which is the same length as the speed array

M-atch:
        For this problem we can use a stack to keep track of the car fleets. 
    We would want to calculate the time it would take to reach the target 
    given a car's position and speed. The formula for this would be:
    time = (target - position) / speed. I think another thing we need to do
    is use list comprehension and the zip function to create a list of tuples
    of the cars with their positions and speeds paired together. We can then
    iterate over the reverse sorted array, this is because we want to evaluate
    the car's from right to left so we can see if a previous car catches up
    to a car on the right. We can then append the time formula onto the stack.
    Then we can have the condition where if there's at least 2 cars on the
    stack and the value on the top of the stack is less than the element
    under it. We can pop the stack, this is because the top element has caught
    up to the element before it and has the same speed of it now. We can then
    return the length of the stack.

P-lan:
    1) Use List Comprehension and zip function to create pairs of position and
       speeds from the input arrays.
    2) Declare our stack
    3) Iterating over the sorted array in reverse
    4) Append the time formula calculation for that car
    5) If the stack has at least 2 cars and the top element is less than the
       2nd to top element
    6) Pop the stack
    7) Return the length of the stack


I-mplement:
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Use List Comprehension to form pairs with a car's position and speed
        pairs = [[p,s] for p, s in zip(position, speed)]

        # Declare our stack
        stack = []

        # Iterating over the sorted array in reverse
        for p, s in sorted(pairs)[::-1]:
            # Append the time formula for the car
            stack.append((target - p) / s)

            # Check if there's at least 2 cars and if the element on the top of the
            # stack is less than the 2nd element from the top
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # Pop the stack
                stack.pop()
        # Return the length of the stack
        return len(stack)


    def display(self, target: int, position: List[int], speed: List[int]) -> None:
        print(f"Input: target = {target}, position = {position}, speed = {speed}")
        print(f"Output:         {self.carFleet(target, position, speed)}\n")

# Testing
sol = Solution()


# Expects 3
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
sol.display(target, position, speed)


# Expects 1
target = 10
position = [3]
speed = [3]
sol.display(target, position, speed)


# Expects 1
target = 100
position = [0,2,4]
speed = [4,2,1]
sol.display(target, position, speed)