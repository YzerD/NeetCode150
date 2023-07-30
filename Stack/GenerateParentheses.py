# LC 22: Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Resources Used: https://www.geeksforgeeks.org/backtracking-algorithms/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input an integer n, that represents the number of pairs of
        parentheses.
    - What is our output?
        Our output is all combinations of well-formed parentheses.
    - What counts as a combination of well-formed parentheses?
        A combination of this form will have a openining parentheses
        before any closing one, meaning that all parentheses are 
        correclty matched.
    - Can our input n be 0?
        No, the constraints state that n can range anywhere from 1 up to 8.


M-atch:
        For this problem we can utilize a stack and backtracking. The reason why
    we're gonna use backtracking is because it is an algorithmic technique
    used for trying to build a solution incrementally, and for the context
    of this problem, we would want to generate all possibile combinations
    for well-formed parentheses. The reason for the stack is to return the
    valid combination and append it to a result list. We can use a helper
    funcion that has the parameters of open and closed parentheses since
    we would have to check if we have reached n of each one. 


P-lan:
    1) Declare our stack
    2) Declare our result list
    3) Define our backtracking helper function with two int parameters, 
       representing a counter for open and closed parentheses
    4) Check if open counter is equal to closed counter which is equal to n
    5) If so, connect the contents of the stack into a string and append it
       to the result list and return
    6) Otherwise, check if the open counter is less than n
    7) If so, append "(" to the stack
    8) Recursively call the backtracking and increment the open counter
    9) Pop the stack so that we can explore other combinations
    10) Check if closed counter is less than open counter
    11) If so, append ")" to the stack
    12) Recursively call the backtracking and increment the closed counter
    13) Pop the stack so that we can explore other combinations
    14) Call the helper function with 0's passed in
    15) Return the result list

I-mplement:
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Declare our stack
        stack = []

        # Declare our result list
        result = []

        # Declare our backtracking helper function
        def backtracking(open, closed):
            # Check if open == closed == n
            if open == closed == n:
                # Combine and append the contents of the stack to the result list
                result.append("".join(stack))
                return
            

            # Check if the open counter is less than n
            if open < n:
                # Push "(" to the stack
                stack.append("(")
                
                # Recursively call the function with updated parameters
                backtracking(open + 1, closed)

                # Pop the element we added to explore other combinations
                stack.pop()

            
            # Check if the closed counter is less than the opne counter
            if closed < open:
                # Push ")" to the stack
                stack.append(")")

                # Recursively call the function with updated parameters
                backtracking(open, closed + 1)

                # Pop the element we added to explore other combinations
                stack.pop()

        
        # Call the backtracking function
        backtracking(0, 0)

        # Return the result list
        return result


    def display(self, n: int) -> None:
        print(f"Input:  n = {n}")
        print(f"Output: {self.generateParenthesis(n)}\n")
        


# Testing
solution = Solution()

# Expects ["((()))","(()())","(())()","()(())","()()()"]
solution.display(3)


# Expects ["()"]
solution.display(1)


"""
R-eview:
    - After trying to come up with a solution, I gave in and watched the
    NeetCode video solution for an idea as to what the solution was. I had
    to review backtracking was and what its use cases were.
    - Looking at the solution I didn't get it at first, thinking about how
    all possible combinations were explored. But I realized that when we first
    call the function the counters aren't equal, so we move on to the check
    where open < n. This is where we push "(" to the stack and recursively 
    call the function. Here, the counters are still not equal to n, but we 
    can explore the case where we can have "((" or "()". Then continue 
    exploring possible combinations
"""