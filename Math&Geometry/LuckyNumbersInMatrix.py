# LC 1380: Lucky Numbers in a Matrix
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
        Our input is an m x n matrix of DISTINCT numbers
    # ? What is our output ?
        Our output is ALL the lucky numbers in the matrix in any order
    # ? What is a lucky number ?
        A lucky number is an element in the matrix such that it is the
        minimum element in its ROW and maximum in its COLUMN.

M-atch:
    For 2D Array's, common patterns for solutions are:
        1) BFS / DFS Search
        2) Hash the 2D Array in some way to help with the strings
        3) Create / Use a Trie

    I don't think any of these common patterns for solutions are applicable, as
    far as I can think of. I think we can first get the dimensions of our input
    matrix and then declare our result list. I think we can iterate over every
    row and col and then declare a variable that stores the value of the current
    element. We can then declare our max and min flags and then iterate through
    every element in the column, checking if our current value is the max in it.
    If it is, we can continue onto the next check, since we need this to be true
    first. We can then check in the row if our current value is the min of it,
    if not we break out and if it is we continue onto the next step. The next
    step being appending it to the result list.

P-lan:
    1) Get dimensions of matrix
    2) Declare result list
    3) Iterating over every row and column
    4) Store the value of the current element and declare our max flag
    5) Iterating over the length of the ROWS, check if current value is
       max
    6) If it isn't set flag to false and break out of loop
    7) If the flag is true continue
    8) Declare our min flag
    9) Iterating over the current row, check if current value is min
    10) If it isn't set flag to false and break out of loop
    11) If the flag is true continue
    12) Append current value to result list
    13) Return result list

I-mplement:
"""

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        # Get dimensions of matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Declare result list
        result = []

        # Iterating over every row
        for row in range(ROWS):
            # Iterating over every columns
            for col in range(COLS):
                # Declare curr_val for this iteration
                curr_val = matrix[row][col]

                # Declare Max flag
                is_max = True

                # Check if current value is max in its column
                for i in range(ROWS):
                    # If it isn't
                    if curr_val < matrix[i][col]:
                        # Set flag to false and break out of loop
                        is_max = False
                        break
                
                # If it's the max in its col, continue
                if not is_max:
                    continue

                # Declare Min flag
                is_min = True
                # Check if current value is min in its row
                for j in range(COLS):
                    # If it isn't
                    if curr_val > matrix[row][j]:
                        # Set flag to false and break out of loop
                        is_min = False
                        break
                
                # If it's the min in its row, continue
                if not is_min:
                    continue

                # Otherwise, it's max in col and min in row, append it to result list
                result.append(curr_val)

        # Return result list
        return result


    def display(self, matrix: List[List[int]]) -> None:
        print(f"Input: matrix = {matrix}")
        print(f"Output:         {self.luckyNumbers(matrix)}\n")

    
# Testing
sol = Solution()


# Expects [15]
matrix = [[3,7,8],[9,11,13],[15,16,17]]
sol.display(matrix)


# Expects [12]
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
sol.display(matrix)


# Expects [7]
matrix = [[7,8],[1,2]]
sol.display(matrix)