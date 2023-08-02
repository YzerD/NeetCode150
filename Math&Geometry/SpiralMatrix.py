# LC 54: Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an m x n matrix
    - What is our output?
        Our output is a list that returns all elements of the matrix in spiral
        order.
    - What is sprial order?
        The sprial order begins at the top left corner of the input matrix, and
        prints all the elements it encounters, while looping towards the center
        of the matrix, in a clockwise manner.
    - Can our input matrix be empty?
        The matrix can't be empty, but the minimum size it can be is a 1 x 1. 

M-atch:
    For 2D Arrays, common solution patterns include:
        1) BFS / DFS Search
        2) Hash the 2D Array in some way to help with Strings
        3) Create / Use a Trie
    
   I think none of the common patterns are applicable for this problem. But similar
   to rotate image, we can utilize four pointers to keep track of what we've 
   encountered so far in the matrix. We can declare our left and right pointers,
   left being 0, and the right being the length of the row. Then we can declare 
   our top and bottom pointers, top being 0 and bottom being the length of the
   columns. Then we can enter our while loop where we go while left < right and
   top is < bottom. We can then iterate the length of the top row, left to right
   and append the values to our result list. After that we can update our top 
   pointer by incrementing it, so we don't include the top right element twice.
   We can then iterate down that column, I think for the length of top and 
   append those values. We then update our right pointer by decrementing it
   so we don't include the bottom right again. We can then have a check if 
   there are no more elements to traverse horizontally and vertically. This can
   be done using the inverse of our while loop condition, so it'd be 
   if not (left < right and top < bottom). The reason for this check is when
   we enter the inner levels of the matrix we go left to right and the top to
   bottom in the rightmost column for that iteration. So this would be our 
   stop point. After that, since we know that there are more elements to 
   traverse. We iterate backwards from bottom right to bottom left and update
   our bottom pointer by decrementing it. We can then finish of by iterating
   bottom left to top left and appending values to the result list, and then
   update our left pointer so we don't include that value again. Finally,
   we can return our result list

P-lan:
    1) Declare our result list
    2) Declare our left and right pointers
    3) Declare our top and bottom pointers
    4) While our left and right pointers haven't met AND our top and bottom
       pointers haven't met
    5) For the length of left to right
    6) Append values of row to result 
    7) Update top pointer
    8) For the length of top to bottom
    9) Append values of column to result
    10) Update right pointer
    11) Check if our pointers have met, and if so break out of while loop
    12) For the length of right to left backwards
    13) Append values of row to result
    14) Update bottom pointer
    15) For the length of bottom to top
    16) Append values to result list
    17) Update left pointer
    18) Return result list


I-mplement:
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Declare our result list
        result = []

        # Declare our pointers
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)


        # While our pointers haven't met
        while left < right and top < bottom:

            # Iterating from left to right
            for i in range(left, right):
                # Append values to list
                result.append(matrix[top][i])
            # Update our top pointer
            top += 1


            # Iterating from top to bottom
            for i in range(top, bottom):
                # Append values to list
                result.append(matrix[i][right - 1])
            # Update our right pointer
            right -= 1


            # Check if our points have nothing left to traverse
            if not (left < right and top < bottom):
                # Break out of the loop
                break


            # Iterating from right to left at the bottom-most row
            for i in range(right - 1, left - 1, -1):
                # Append values to list
                result.append(matrix[bottom - 1][i])
            # Update our bottom pointer
            bottom -= 1

            # Iterating from bottom to top at left-most column
            for i in range(bottom - 1, top - 1, -1):
                # Append values to list
                result.append(matrix[i][left])
            # Update our left pointer
            left += 1
        
        # Return result list
        return result


    def display(self, matrix: List[List[int]]) -> None:
        print(f"Input: matrix = {matrix}")
        print(f"Output:         {self.spiralOrder(matrix)}\n")


# Testing
solution = Solution()


# Expects [1,2,3,6,9,8,7,4,5]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.display(matrix)

# Expects [1,2,3,4,8,12,11,10,9,5,6,7]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution.display(matrix)