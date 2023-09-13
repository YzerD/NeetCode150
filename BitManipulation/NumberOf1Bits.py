# LC 191: Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Yzer De Gula

"""
U-nderstand:
    # ? What is our input ?
        - Our input is a 32-bit integer
    # ? What is our output ?
        - Our output is the number of 1 bits in the integer
    # ? What is the range of our input ?
        - Our input is a 32-bit integer
    # ? What is the range of our output ?
        - Our output is an integer  [0, 32]
    # ? Do we have constraints ?
        - No constraints
    # ? What if the input is 0 ?
        - Return 0

M-atch:
        For this problem, we can use the modulo operator to get the last bit of
    the integer. We can then add that to our result. We can then shift the
    integer to the right by 1 to get the next bit. We can continue this process
    until the integer is 0. We can then return our result.
    
P-lan:
    1) Declare our result variable
    2) While n is not 0
        i) Add the last bit of n to the result
        ii) Shift n to the right by 1
    3) Return the result
        
I-mplement:
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Declare our result variable
        result = 0

        # While n is not 0
        while n:
            # Add the last bit of n to the result
            result += n % 2
            # Shift n to the right by 1
            n = n >> 1
        # Return the result
        return result
    

    def display(self, n: int) -> None:
        print(f"Input: n = {n}")
        print(f"Output: {self.hammingWeight(n)}\n")


# Testing
test = Solution()

# Expects 3
test.display(0b00000000000000000000000000001011)

# Expects 1
test.display(0b00000000000000000000000010000000)

# Expects 31
test.display(0b11111111111111111111111111111101)