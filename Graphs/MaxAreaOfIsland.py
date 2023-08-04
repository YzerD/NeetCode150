# LC 695: Max Area of Island
# https://leetcode.com/problems/max-area-of-island/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ?
      Our input is a m x n binary matrix named grid. Some things we can say
      about our input is that since it's binary, we know that the elements can
      either be a 1 or a 0.
    # ? What is our output ?
      Our output is the maximum area of an island in grid. If there is no 
      island, return 0
    # ? What is considered an island ?
      An island is a group of 1's (representing land) connected horizontally
      and vertically (not diagonally). 
    # ? Can our input matrix be empty?
      No, the constraints state that the minimum m and n can be is 1.
    
      
M-atch:
    For Graph problems, common patterns for solutions include:
        1) DFS
        2) BFS
        3) Union Find
        4) Adjacency List
        5) Adjacency Matrix
        6) Topological Sort
    
        For this problem, I think we can use DFS to find the area of an island
    whenever we encounter a 1. We can recursively call DFS on that element
    to check neighboring elements. This is similar to the Number of Islands
    Problem, where we can utilize a Hash Set to keep track of entires we have
    visited. First thing we can do is get the dimensions of the input matrix.
    We can then declare our dfs helper function that takes in the element's
    row and column that we are checking. Since DFS is typically recursive, we
    need to have a base case, in order to know when we should stop the calls.
    This can be if the indicies are out of bounds row < 0 or col < 0 or
    row == ROWS or col == COLS. Other conditions we need to check if it's 
    water and we haven't visited it already grid[row][col] == 0 or (row, col)
    not in visited. If any of these are true, we return 0. Otherwise, we add
    that coordinates to the set and recursively call the function with 1 + 
    with the neighboring elements. The 1 + is to acount for the node we just
    checked. Then in the outside function we iterate over the rows and cols
    and then check if the element is a 1 and not in visited, if this is true
    we can take the max of the current max and the DFS call. We can then return
    the max area.

P-lan:
    1) Get the dimensions of our input matrix
    2) Declare our Hash Set
    3) Declare our Max Area variable
    4) Declare our DFS helper function that takes in the row and columns of the
       element that we are checking
    5) BASE CASE: Check if element is out of bounds, or is 0, or is visited,
       return 0
    6) Otherwise, add it to the Hash Set
    7) Return 1 + the recursive call for the sum of the neighboring elements
    8) In the outside function, iterating over every row
    9) Iterating over every col
    10) Take the max of the current max and the dfs call on that element
    11) Return max area 


I-mplement:
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the dimensions of our input matrix
        ROWS, COLS = len(grid), len(grid[0])

        # Declare our Hash Set and Max Area variable
        visited, max_area = set(), 0

        # Declare our DFS helper function
        def dfs(row, col):
            # BASE CASE
            if (row < 0 or 
                col < 0 or
                row == ROWS or 
                col == COLS or
                grid[row][col] == 0 or
                (row, col) in visited):
                
                # Return 0
                return 0
            
            # Otherwise, add it to hash set
            visited.add((row, col))

            # Recursively call the function on the neighboring elements
            return 1 + dfs(row + 1, col) \
                     + dfs(row - 1, col) \
                     + dfs(row, col + 1) \
                     + dfs(row, col - 1)
        
        # Iterating over every row
        for i in range(ROWS):
            # Iterating over every columns
            for j in range(COLS):
                # Take the max of the current max and the DFS call on the element
                max_area = max(max_area, dfs(i, j))

        # Return max area
        return max_area



    def display(self, grid: List[List[int]]) -> None:
        print(f"Input: grid = {grid}")
        print(f"Output:       {self.maxAreaOfIsland(grid)}\n")


# Testing
sol = Solution()

# Expects 6
grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
sol.display(grid)


# Expects 0
grid = [[0,0,0,0,0,0,0,0]]
sol.display(grid)


"""
R-eview:
    - Slight typo on the return call on the outside function, had return max
      instead of retrun max_area.

E-valuate:
    - The runtime of this algorithm is O(m * n) since we're checking at worst
      every element in the input matrix. The memory should also be O(m * n),
      since at worst we have to store every element into our Hash Set.
"""