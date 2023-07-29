# LC 150: Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an array of strings (tokens) that represent an
        arithmetic expression in a Reverse Polish Notation
    - What is our output?
        Our output is an integer which is the evaluation of the expression.
    - What are the valid operators?
        Valid operators are "+", "-", "*", and "/"
    - Is there a chance that an invalid character or operator is in our input?
        The constraints state that an element in our input array is either an
        operator "+", "-", "*", "/", or an integer in the range -200 to 200.
    - Can our input array be empty?
        No, the minimum length of the input array is 1

M-atch:
    For this problem we can use a stack to keep track of the numbers and for
    everytime we reach a number, we push that onto the stack. Once we reach
    an operator, we can then perform the operation.In the case of addition, 
    we need to pop off the top 2 numbers on the stack and append that value.
    We'll do the same for the rest of the operations.

P-lan:
    1) Declare our stack
    2) Iterating over the length of the input array
    3) If the element is a number, push it onto the stack
    4) If the element is a "+", we append the addition of the two top numbers
    5) If the element is a "-", we append the subtraction of the top two numbers
    6) If the element is a "*", we append the multiplication of the top two numbers
    7) If the element is a "/", we append the division of the top two numbers
    8) Return the top of the stack

    A thing we have to keep in mind is the operation of subtraction and division.
    For these operations, order matters, unlike multiplication and addition. So 
    I think we can pop the stack and store them into two temp variables, and then
    append the operation with the correct order of the values. Thinking about the
    logic of the if statements, I think it would be better to have if it's a
    number at the end, since there's such a vast range.

I-mplement:
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Declare our stack
        nums_stack = []

        # Iterating over the length of the input array
        for i in range(len(tokens)):
            # Check if the element is a "+"
            if tokens[i] == "+":
                # Append the addition of the top two elements
                nums_stack.append(nums_stack.pop() + nums_stack.pop())
            
            # Check if the element is a "-"
            elif tokens[i] == "-":
                # Store the top two elements into temp variables
                nums1, nums2 = nums_stack.pop(), nums_stack.pop()

                # Append the subtraction of the top two elements
                nums_stack.append(nums2 - nums1)

            # Check if the element is a "*"
            elif tokens[i] == "*":
                # Append the multiplication of the top two elements
                nums_stack.append(nums_stack.pop() * nums_stack.pop())
            
            # Check if the element is a "/"
            elif tokens[i] == "/":
                # Store the top two elements into temp variables
                nums1, nums2 = nums_stack.pop(), nums_stack.pop()

                # Append the division of the top two elements
                nums_stack.append(int(nums2 / nums1))

            # Otherwise, the element is a number
            else:
                # Push that number onto the stack
                nums_stack.append(int(tokens[i]))
            
        # Return the top of the stack
        return nums_stack[0]
    

    def display(self, tokens: List[str]) -> None:
        print(f"Input:  {tokens}")
        print(f"Output: {self.evalRPN(tokens)}\n")


# Testing
solution = Solution()


# Expects 9
tokens = ["2","1","+","3","*"]
solution.display(tokens)


# Expects 6
tokens = ["4","13","5","/","+"]
solution.display(tokens)


# Expects 22
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution.display(tokens)


"""
R-eview:
    - There seems to be an error with the division. It's giving decimals,
      but upon reading back to the problem's specifications, it states that
      division always truncates towards 0. So I think to remedy this, we do
      a floor division. 
    - That solved one test case, but it bothced another one. 
    - I think instead of doing floor division, since when we divide it 
      results into a float, we can just convert that back to an int.
    - That worked (:

E-valuate:
    - The runtime of this algorithm should be O(n) since we have to evaluate
      the entire input array.
    - The space of this algorithm should also be O(n) due to the stack.
"""