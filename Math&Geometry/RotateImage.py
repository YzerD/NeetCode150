# LC 48: Rotate Image
# https://leetcode.com/problems/rotate-image/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an n x n 2D matrix called matrix.
    - What is our output?
        Our output is the matrix rotated 90 degrees (clockwise).
    - Can we allocate a new array to return?
        No, the problem specifies that we must modify the original input
        in-place.
    - Can our input be empty?
        No, the constraints state that the minimum length of the input matrix
        is 1 x 1
    

M-atch:
    For this problem, since we have to modify in-place, we have to keep track
    of the four positions in the outer region first. Top-Left, Top-Right, 
    Bottom-Left, Bottom-Right. We can declare two pointers, for our left and
    right. Then declare a while loop so that until our pointers crossed and
    then declare our top and bottom pointers, these are gonna be the same as
    the left and right pointers. We can then iterate for the squares by doing
    r - l. Take a 4 x 4 square matrix for instance, there's an outer 4 x 4
    square, and an inner 2 x 2 square. So we can iterate through r - l (3 - 0)
    to iterate through that, then when we update our pointers our inner square
    loop would be 2 - 1 = 1. Which is expected since for loops start at 0.
    As for the rotating, we can first store the top left element, and then
    store the BL element there, then the BL gets the BR, and the BR gets the
    TR, then TR gets the previously stored TL element. The reason for this
    is because if we did the rotating clockwise, we'd have to continuously
    store a temp value, the counter-clockwise method bypasses this.


P-lan:
    1) Declare our left and right pointers
    2) While our two pointers haven't crossed
    3) Declare our top and bottom pointers 
    4) Iterating over the outer square first (right - left)
    5) Store the top left element
    6) Store the bottom left element in the top left 
    7) Store the bottom right element in the bottom left
    8) Store the top right element in the bottom right
    9) Store the stored top left element in the top right
    10) Update our pointers to get inner squares


I-mplement:
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Declare our left and right pointers
        left, right = 0, len(matrix) - 1

        # While our two pointers haven't crossed
        while left < right:
            # Iterating over the outer square
            for i in range(right - left):


                # Declare our top and bottom pointers
                top, bottom = left, right

                # Store the top left element
                top_left = matrix[top][left + i]

                # Store the bottom left element in the top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # Store the bottom right element in the bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # Store the top right element in the bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # Store the stored top left element in the top right
                matrix[top + i][right] = top_left
                

            # Update our pointers to get inner squares
            left += 1
            right -= 1



    def display(self, matrix: List[List[int]]) -> None:
        print(f"Input: matrix = {matrix}")
        self.rotate(matrix)
        print(f"Output:         {matrix}\n")


# Testing
solution = Solution()


# Expects [[7,4,1],[8,5,2],[9,6,3]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.display(matrix)


# Expects [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.display(matrix)
