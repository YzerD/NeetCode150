# LC 463: Island Perimeter
# https://leetcode.com/problems/island-perimeter/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is a 2D-Array that is row x col where a value of 1 represents
        land and a 0 represents water
    - What is our output?
        Our output is the perimeter of the island
    - How is the island connected?
        The island is connected only horizontally and vertically, but not 
        diagonally. There is also exactly one island.
    - Can our input be empty?
        No, in the constraints, the minimum size of our input is 1 x 1

        
M-atch:
    For 2D-Arrays, common solution patterns include:
        1) BFS / DFS Search
        2) Hash the 2D-Array 
        3) Create / Use a Trie
    
    This problem doesn't seem to adhere to our common techniques. What we know is
    that we only need to check the neighboring cells of a land node. So we have
    to iterate over the 2D-Array and check if that cell is equal to 1 (land). We
    can then check if the cell is an edge of the 2D-Array or the neighbor is
    equal to 0 (water) and then increment a perimeter counter. The left neighbor
    is (row, col - 1), right neighbor is (row, col + 1). Top neighbor is 
    (row - 1, col) and bottom neighbor is (row + 1, col). The edge cases we have
    to look our for is if the cell's row = 0, col = 0, row = rows - 1, and
    col = cols - 1. We then return the perimeter variable.


P-lan:
    1) Declare our perimeter variable
    2) Get the lengths of our rows and columns
    3) Iterating over every row
    4) Iterating over every col
    5) Check if the current cell is equal to 1
    6) Check if left neighbor is an edge or is water, if so increment perimeter
    7) Check if top neighbor is an edge or is water, if so increment perimeter
    8) Check if right neighbor is an edge or is water, if so increment perimeter
    9) Check if bottom neighbor is an edge or is water, if so increment perimeter
    10) Return perimeter

I-mplement:
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Declare our perimeter var
        perimeter = 0

        # Get lengths of grids row and columns
        rows, cols = len(grid), len(grid[0])

        # Iterating over the entire 2D-Array
        for row in range(rows):
            for col in range(cols):
                # If the cell is land
                if grid[row][col] == 1:

                    # Check if left neighbor is edge or is water
                    if col == 0 or grid[row][col - 1] == 0:
                        # If so add 1 to perimeter
                        perimeter += 1

                    # Check if top neighbor is edge or is water
                    if row == 0 or grid[row - 1][col] == 0:
                        perimeter += 1

                    # Check if right neighbor is edge or water
                    if col == cols - 1 or grid[row][col + 1] == 0:
                        perimeter += 1

                    # Check if bottom neighbor is edge or water
                    if row == rows - 1 or grid[row + 1][col] == 0:
                        perimeter += 1
        
        # Return perimeter variable
        return perimeter


    def display(self, grid: List[List[int]]) -> None:
        print(f"Input: grid = {grid}")
        print(f"Output: {self.islandPerimeter(grid)}\n")


# Testing
solution = Solution()

# Expects 16
grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
solution.display(grid)


# Expects 4
grid = [[1]]
solution.display(grid)


# Expects 4
grid = [[1,0]]
solution.display(grid)
