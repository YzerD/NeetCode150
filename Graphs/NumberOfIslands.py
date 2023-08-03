# LC 200: Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Yzer De Gula

from typing import List
from collections import deque

"""
U-nderstand:
    ? What is our input ?
      - Our input is an m x n 2D binary grid called grid. The grid represents
        a map of "1's" (land) and "0's" (water)
    ? What is our output ?
      - Our output is the number of islands
    ? What is considered an island ?
      - An island is surrounded by water and is formed by connecting adjacent
        lands horizontally or vertically (not diagonally). 
    ? Can our input matrix be empty ?
      - No, the minimum our matrix can be is a 1 x 1 matrix


M-atch:
    For Graph problems, common patterns for solutions include:
        1) DFS
        2) BFS
        3) Union Find
        4) Adjacency List
        5) Adjacency Matrix
        6) Topological Sort

      For this problem, I think we can either use a BFS or DFS traversal to keep
    track of which elements we've visited and to check neighboring elements if
    they're "1's" as well. 

      The first check we should make is whether there even is a grid to process.
    In the event of this, we should return 0, because there are 0 islands.
    We should also declare a set to make sure that we don't check the same 
    element twice. We can then get the dimensions of our matrix and store them
    into variables. This will be used for traversing the matrix. We can also 
    declare a variable to act as a counter for the number of islands.
    
      We can then declare our BFS helper function, the parameters should be the
    row and col of the element we're checking. We can first declare our 
    double-ended queue and add the coordinates of the entry to our set and also
    to our queue. While there is something in our queue, we pop the front of
    the queue and then declare a list of neighboring indicies that are only
    horizontal and vertical to the current element. Iterating over the 
    neighboring elements list, we calculate the index of the neighbor by 
    adding the row and col of our current element to the values from the list.
    We then check if the neighbor is actually within the range of the matrix
    and if so, we'd append it to the queue and mark it in our visited set.

      After we've finished the implementation of our BFS search we can call it
    in the outside function. Iterating over every row and column in our matrix,
    if the element is land (1), and we haven't visited it, call the bfs 
    function on the element and then increment our island counter. After this
    loop ends, we can return the island counter.


P-lan:
  1) Check if there is no grid to check, if so return 0
  2) Declare our set
  3) Declare our island counter
  4) Get the dimensions of our matrix
  5) Declare our BFS helper function that takes in the row and column of the
     element we're checking
  6) Declare our deque
  7) Add the coordinates of the element to our set
  8) Append coords to queue
  9) While there is something in our queue
  10) Pop the front of the queue 
  11) Declare a list of neighboring elements that we can iterate through
  12) Iterating over the neighboring list
  13) Calculate the coordinates of the current neighbor we're checking
  14) Check if the coordinates are in the range of the matrix
  15) If so, append the coords of that into the queue and in set
  16) Iterating over every row
  17) Iterating over every column
  18) If the element is a "1" and isn't in our set
  19) Call the BFS helper function on that element
  20) Increment Island counter
  21) Return Island counter

I-mplement:
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if grid is empty
        if not grid:
            # Return 0
            return 0
        
        # Declare our set, island count, and get dimensions
        visited = set()
        island_count = 0
        ROWS, COLS = len(grid), len(grid[0])

        # Declare BFS helper function
        def bfs(row, col):
            # Declare our deque
            queue = deque()

            # Add element to set
            visited.add((row, col))

            # Add element to queue
            queue.append((row, col))

            # While there is something in our queue
            while queue:
                # Pop the front of the queue
                current_row, current_col = queue.popleft()

                # Declare a list that represents the neighboring elements
                neighbors = [[0,-1], [0,1], [1,0], [-1,0]] 

                # ! Issue with reusing the same row and col variable names
                # Iterating over the neighbor list
                for neighbor_row, neighbor_col in neighbors:
                    # Calculate the index of the neighbor
                    new_row, new_col = current_row + neighbor_row, current_col + neighbor_col

                    # If the neighbor is in the range of the matrix
                    if new_row in range(ROWS) and new_col in range(COLS) \
                    and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        # Add coords to queue
                        queue.append((new_row, new_col))

                        # Add coords to set
                        visited.add((new_row, new_col))
        
        # Iterating over every row
        for row in range(ROWS):
            # Iterating over every col
            for col in range(COLS):
                # If the element is a 1 and isn't in our set
                if grid[row][col] == "1" and (row, col) not in visited:
                  # Call the helper function on this element
                  bfs(row, col)
                  # Increment island counter
                  island_count += 1

        # Return Island count
        return island_count


    def display(self, grid: List[List[str]]) -> None:
        print(f"Input: grid = {grid}")
        print(f"Output:       {self.numIslands(grid)}\n")


# Testing
solution = Solution()


# Expects 1 
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
solution.display(grid)


# Expects 3
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
solution.display(grid)


# Expects 1
# ! Outputs 2
grid = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
solution.display(grid)

"""
R-eview:
  I've spent an absurd amount of time on this problem, even after watching
the video solution and looking at the solution. I have a decent understanding
of the BFS algorithm, but applying it to a matrix / graph seemed very foreign
to me. I finally got it to work after debugging for a while. The first issue
was trying to put the append of the current element in the the constructor
of the deque. This caused a TypeError: cannot unpack non-iterable int object.
The second issue was entirely my fault. I was using the same variable name, row
and columns in the BFS helper function. So that was causing some unexpected 
outputs. But after that, this was accepted in LeetCode, albeit with not the
best Space Time Complexity. 
"""