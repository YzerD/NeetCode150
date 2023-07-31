# LC 739: Daily Tempeartures
# https://leetcode.com/problems/daily-temperatures/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an array of integers, temperatures that represent the daily
      temperatures.
    - What is our output?
        Our output is the number of days you have to wait after the ith day to
        get a warmer temperatures. If there are no future day for which this is
        possible, keep answer[i] == 0 instead.
    - Can our input be empty?
        No, the constraints state that the minimum length of the input array is
        1 and can go up to 10^5.


M-atch:
    For this problem we can use a stack. The stack will be used for keeping
    track of the index of a temperature until we find a higher temperature.
    Similar to the Product of Array Except Self, we can initialize our result
    list with 0's multiplied by the length of the input array to handle the
    cases where there are no future days. As for our stack, we want to make
    sure that there is something in the stack to compare and that the current
    temperature is greater than the top of the stack. This is because when
    we have reached a greater temp in the current iteration we want to 
    update our result array. To do this, we have to pop the top of the
    stack and store it in a variable, we can then use that value to get
    the exact index of the result array and set the value of that index to
    the difference of the current iteration and the index that the value
    represents. This should all be in a while loop to check if the any
    other values on the stack or less than the current value in this 
    iteration. Otherwise, we know that the stack is empty or that its
    a lesser value than what's on the stack, and therefore we push it
    onto the stack.


P-lan:
    1) Declare our stack
    2) Declare our result array that's the same length as the input array 
    initialized with 0's.
    3) For the length of the input array
    4) While there is something in the stack, and the value of the input array
       indexed at our current iteration is greater than that of what's on top
       of the stack
    5) We pop the stack and store it into a variable
    6) We then index the result array at the value and set the value of that to
       the difference of the current iteration and the variable
    7) Otherwise, we know that the stack is either empty or is a lesser value 
       compared to what's on top of the stack.
    8) Return the result list.

I-mplement:
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Declare our stack
        stack = []
        
        # Declare our result array with default values of 0's of the same
        # length as input array
        result = [0] * len(temperatures)

        # Iterating over the entire length of the input array
        for i in range(len(temperatures)):

            # While there is something in our stack and the value held at that
            # index is greater than what's on top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:


                # We pop the top of the stack and store it
                prev_index = stack.pop()


                # At that index in the result array, store the difference of the
                # current iteration and the index
                result[prev_index] = i - prev_index


            # Otherwise, we know that either the stack is empty or the value is
            # lesser to what is stored on top of the stack
            stack.append(i)
        
        # Return our result list
        return result


    def display(self, temperatures: List[int]) -> None:
        print(f"Input: temperatures = {temperatures}")
        print(f"Output:               {self.dailyTemperatures(temperatures)}\n")


# Testing 
solution = Solution()


# Expects [1,1,4,2,1,0,0]
temperatures = [73,74,75,71,69,72,76,73]
solution.display(temperatures)


# Expects [1,1,1,0]
temperatures = [30,40,50,60]
solution.display(temperatures)


# Expects [1,1,0]
temperatures = [30, 60, 90]
solution.display(temperatures)