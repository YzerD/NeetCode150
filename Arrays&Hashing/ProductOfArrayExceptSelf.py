# LC 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Resource: https://www.geeksforgeeks.org/enumerate-in-python/#
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an integer array nums
    - What is our output?
        Our output is an array answer such that each index in the array is
        equal to the product of all the other elements of nums except itself
    - The Problem emphasizes that the algorithm should have a runtime of O(n)
      and doesn't use the division operation.
    - Can the array be empty?
        No, the constraints of the problem state that the minimum length of the
        input array is 2
    - Can the value of an index of the array be 0?
        Yes, the numbers in the input array can range from -30 up to and
        including 30.

M-atch:
    With arary and string problems, common patterns for their solutions are:
        1) Sorting
        2) Sliding Window
        3) Two Pointers
        4) Store in Hash Map or Set
    
    Sorting won't help since for multiplication the position of the integers
    don't matter. Storing the elements into a Hash Map can help, we can have
    the value as the key and the index as the value. We can then iterate over
    the map for the length of the array and while the current iteration isn't
    equal to the value (index) in the map we can have a running product of 
    every other element and append it to result. 

P-lan:
    1) Create our Hash Map and answer array
    2) Store the input array into our Hash Map with the keys as the values
       and their index as the value
    3) Create temp vars for a key and value 
    4) Iterating over the map for the length of the array
    5) If the iteration is NOT the equal to the value (index) multiply the
       running product by the key of that value.
    6) Return the answer array.

I-mplement:
"""

def productExceptSelf(nums: List[int]) -> List[int]:
    # Create our Hash Map
    nums_map = dict()

    # Create our answer array
    answer = []

    # Store the elements of the input array into our Hash Map
    # Having the values as the keys and their index as the value
    for i, num in enumerate(nums):
        nums_map[num] = i

    # Over the length of the array
    for i in range(len(nums)):
        product = 1
        # Calculate the product excluding the current element
        for key, value in nums_map.items():
            if (i != value):
                product *= key
        
        # Append the prodcut to the answer array
        answer.append(product)
    
    # Return answer array
    return answer

"""
R-eview:
    - Learned about the enumerate() function in Python, it returns tuples of
      the form (index, value). So that drastically helped declutter the code
      for storing the input array into the Hash Map.
    - Putting this into LeetCode it doesn't pass all the Test Cases, it 
      passes 10/22. 
E-valuate:
    - Runtime is O(n^2) which is bad since the problem specified O(n)
    - Space is O(n) since we stored all of the input array into a Hash Map
"""

# From NeetCode
def productExceptSelfOptimal(nums: List[int]) -> List[int]:
    # Create an initial list filled with 1's of the same length as the input array
    res = [1] * (len(nums))
    
    # Create our prefix var that represents as the running product of all
    # elements to the left of the current element
    prefix = 1

    # Iterating over the length of the input array
    for i in range(len(nums)):
        # Set the current index of the result list to that of the prefix
        res[i] = prefix
        # Update the prefix by multiplying the current element to the running product
        prefix *= nums[i]

    # Create our postfix var that represents as the running product of all
    # elements to the right of the current element
    postfix = 1

    # Iterating over the input array but in reverse
    for i in range(len(nums) - 1, -1, -1):
        # Multiply the current index of the result list to that of the postfix
        # This effectively multiples the prefix and postfix together
        res[i] *= postfix
        # Update the postfix by multiplying the current element to the running product
        postfix *= nums[i]

    # Reutrn the result array
    return res

"""
Why NeetCode's solution works:
https://www.youtube.com/watch?v=bNvIQI2wAjk

Prefix Product: At element nums[i] the prefix product is all the elements
to the left of the element (not including the element itself)

Postfix Product: At element nums[i] the postfix product is all the elements
to the right of the element

So if we multiply everything from the left of the current element by everything
to the right of the current element, that would result in the product excluding
the current element itself.

Take the first Test Case where nums = [1,2,3,4]
The Prefix Product of this array results in:
    prefix[0] = 1, since there are no elements to the left of nums[0]
    prefix[1] is calculated by prefix[0] * nums[0] = 1 * 2 = 2
    prefix[2] is calculated by prefix[1] * nums[1] = 2 * 3 = 6
    prefix[3] is calculated by prefix[2] * nums[2] = 6 * 4 = 24

    This results in the prefix array being [1,2,6,24]

The Postfix Product of this array results in:
    postfix[3] = 4 since there are no elements to the right of nums[3]
    postfix[2] is calculated by postfix[3] * nums[2] = 4 * 3 = 12
    postfix[1] is calculated by postfix[2] * nums[1] = 12 * 2 = 24
    postfix[0] is calculated by postfix[1] * nums[0] = 24 * 1 = 24

    This results in the postfix array being [24,24,12,4]

For the current index in the nums array, if we multiply every prefix element
(left of the current index) by the postfix element to the right of the current
index we would get the product of everything except itself. 
    nums    = [ 1,  2,  3,  4 ]
    prefix  = [ 1,  2,  6,  24]
    postfix = [ 24, 24, 12, 4 ]
    result  = [ 24, 12, 8,  6 ]

For result[0]:
    nums[0]    = 1 
    prefix     = 1 (There is nothing to the left of this element so default is 1)
    postfix[1] = 24
    result = (prefix * postfix) = (1 * 24) = 24

For result[1]:
    nums[1]    = 2
    prefix[0]  = 1
    postfix[2] = 12
    result = (prefix * postfix) = (1 * 12) = 12

For result[2]:
    nums[2]    = 3
    prefix[1]  = 2
    postfix[3] = 4
    result = (prefix * postfix) = (2 * 4) = 8

For result[3]
    nums[3]   = 4
    prefix[2] = 6
    postfix   = 1 (There is nothing to the right of this element so default is 1)
    result = (prefix * postfix) = (6 * 1) = 6

This is why he creates a initial results list of 1's to cover the cases at the 
end of Prefix and Postfix Products in the code

This has a Time Complexity of O(n) and a Space Complexity of O(1)
"""


# Expects [24,12,8,6]
nums_1 = [1,2,3,4]
print("Naive Solution:   ", productExceptSelf(nums_1))
print("Optimal Solution: ", productExceptSelfOptimal(nums_1))

# Expects [0,0,9,0,0]
nums_2 = [-1,1,0,-3,3]
print("Naive Solution:   ", productExceptSelf(nums_2))
print("Optimal Solution: ", productExceptSelfOptimal(nums_2))