# LC 867: Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/
# Resources Used: https://www.cuemath.com/algebra/transpose-of-a-matrix/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is a 2D integer array named matrix
    - What is our output?
        Our output is the transpose of that matrix
    - What is a transpose?
        A transpose is the matrix flipped over its main diagonal,
        switching the matrix's row and column indices.
    - Can our input matrix be empty?
        No, the minimum our matrix can be is a 1 x 1.

    Happy Case:
    Input: matrix = [[1,2,3],[4,5,6]]
    Output: [[1,4],[2,5],[3,6]]

    Input: matrix = [[2,4],[8,16]]
    Output: [[2,8],[4,16]]

    Edge Case:
    Input: matrix = [[1]]
    Output: [[1]]

M-atch:
    For this problem, we have to keep in mind the nature of a tranposition
    of a matrix. Given a non-square matrix the rows become the columns and
    the columns become the rows in the new matrix. Knowing that, we can get
    the dimensions of the original matrix, and then create a new matrix that
    is columns x rows. We can then iterate over the rows of the original,
    iterating over the columns as well, and can swap the indices of the rows
    and columns We can then return the new matrix


P-lan:
    1) Get dimensions of original matrix
    2) Create new matrix with columns x rows of original dimensions
    3) Itearting over every row in the original
    4) Itearting over every column in the original
    5) Swap the matrix's row and column indices.
    6) Return the new matrix

I-mplement:
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Get dimensions of original array
        rows, columns = len(matrix), len(matrix[0])


        # Create new matrix
        """
        Using List Comprehension, we can generate an empty array with the
        dimensions of col x row. The outer loops runs columns times and the
        inner loop runs rows times and fills the positions with a 0.
        """
        transpose_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

        # Iterating over the rows
        for i in range(rows):
            # Iterating over the columns
            for j in range(columns):
                # Swap the rows and column indices
                transpose_matrix[j][i] = matrix[i][j]

        # Return the transposed matrix
        return transpose_matrix


    def display(self, matrix: List[List[int]]) -> None:
        print(f"Input: matrix = {matrix}")
        print(f"Output:         {self.transpose(matrix)}\n")


# Testing
solution = Solution()

# Expects [[1,4,7],[2,5,8],[3,6,9]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.display(matrix)


# Expects [[1,4],[2,5],[3,6]]
matrix = [[1,2,3],[4,5,6]]
solution.display(matrix)


# Expects [[1]]
matrix = [[1]]
solution.display(matrix)
