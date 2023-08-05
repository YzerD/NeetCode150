# LC 509: Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/
# Yzer De Gula

"""
U-nderstand:
    # ? What is our input ?
        - Our input is an integer n
    # ? What is our output ?
        - Our output is the calculate F(n), referring to the number at the
          nth position in the Fibonacci sequence
    # ? What is the Fibonacci Sequence ?
        - The Fibonacci sequence, is a sequence such that each number is the
          sum of the two preceding ones, starting from 0 and 1.

M-atch:
    We can solve this problem recursively, since we know the base cases for
    this sequence. That being when n is equal to 0 or 1, in this case, we can
    return n. Otherwise, we can return the recursive call of fib(n - 1) + 
    fib(n - 2)


P-lan:
    1) Base Case: If n == 0 or n == 1, return n
    2) Return the recursive call of n - 1 + n - 2

I-mplement:
"""

class Solution:
    # Recursive
    def fib(self, n: int) -> int:
        # Base Case: if n == 0 or n == 1
        if n == 0 or n == 1:
            return n

        # Otherwise, return the recursive call of n - 1 + n - 2
        return self.fib(n - 1) + self.fib(n - 2)
    

    # Dynamic Programming
    def fibDynamic(self, n: int) -> int:
        # Create an array with our sequence's starting values
        fib = [0,1]

        # Starting from our base cases up to n (end point is non-inclusive hence + 1)
        for i in range(2, n + 1):
            # Calculate and append the termsn of the sequence
            fib.append(fib[i - 1] + fib[i - 2])

        # Return the value stored at index n
        return fib[n]


    def display(self, n: int) -> int:
        print(f"Input: n = {n}")
        print(f"Output: Recursive = {self.fib(n)}")
        print(f"        Dynamic   = {self.fibDynamic(n)}\n")
    

# Testing
sol = Solution()


# Expects 1
n = 2
sol.display(n)

# Expects 2
n = 3
sol.display(n)

# Expects 3
n = 4
sol.display(n)