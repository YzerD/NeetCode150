# LC 36: Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/
# Yzer De Gula

from typing import List
import collections

"""
U-nderstand:
    What is our input?
        - Our input is a List of Lists representing a 9 x 9 sudoku board that
          contains strings and not ints
    What is our output? 
        - Our output is a Boolean value where True means that the board is
          valid and False if not
    What does it mean for a board to be valid?
        - To be valid each row, column, and 3x3 subgrid must contain the digits
          1 - 9 without repetition.
    What represents an empty square?
        - Empty squares are represented by a period: "."
    In the board can there be any other characters that aren't 1-9 or .?
        - In the constraints every entry in the board is a 1-9 or .
    Can the board's length not be 9 x 9?
        - In the constraints, the problem states that the board lengths row and
          column wise is 9

M-atch:
    For array and string problems, common patterns for their solution is:
        1) Sorting
        2) Sliding Window
        3) Two Pointers
        4) Storing in Hash Map or Set

    Sorting wouldn't be a viable option since we need to check if an entry's
    position are distinct. Sliding window or Two Pointer wouldn't help. So
    I think similar to contains duplicate we need to store the elements
    in a set for the row, column, and subgrid. To get the subgrid I think
    we can do the entries row and column the value subtracted by the value
    mod 3. So the subgrids we go from:

        Topleft:            TopMiddle:          TopRight:
            row = 0 - 3         row = 3 - 6         row = 6 - 9
            col = 0 - 3         col = 0 - 3         col = 0 - 3

        MiddleLeft:         MiddleMiddle:       MiddleRight:
            row = 0 - 3         row = 3 - 6         row = 6 - 9
            col = 3 - 6         col = 3 - 6         col = 3 - 6
        
        BottomLeft:         BottomMiddle:       BottomRight:
            row = 0 - 3         row = 3 - 6         row = 6 - 9
            col = 6 - 9         col = 6 - 9         col = 6 - 9

    Take board[5][7] for instance, Row = 5 - (5 % 3) = 3 , Col = 7 - (7 % 3) = 6
    This places this position in the BottomMiddle subgrid which is what is expected.

P-lan:
    1) Declare our sets for the row, col, and subgrid
    2) Iterating over every row (9)
    3) Itearting over every column (9)
    4) If the entry is a period (Empty), continue
    5) If the entry is present in the row, col, or subgrid
    6) Return False
    7) Otherwise, add that entry to the sets
    8) After all the iterations return True

I-mplement:
"""
def isValidSudokuWrong(board: List[List[str]]) -> bool:
    row_set = [set() for _ in range(9)]
    col_set = [set() for _ in range(9)]
    subgrid_set = [set() for _ in range(9)]

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
                
            if (
                board[row][col] in row_set[row] or
                board[row][col] in col_set[col] or
                board[row][col] in subgrid_set[(row - (row % 3), col - (col % 3))]):
                return False

            row_set[row].add(board[row][col])
            col_set[col].add(board[row][col])
            subgrid_set[row - (row % 3)][col - (col % 3)].add(board[row][col])
    
    return True

# From NeetCode:
def isValidSudoku(board: List[List[str]]) -> bool:
    # Create Hash Sets to keep tracks of numbers we've seen in rows, cols, and subgrids
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    subgrids = collections.defaultdict(set)

    # Iterating over every row,
    for row in range(9):
        # Iterating over every column,
        for col in range(9):
            # If the entry is empty (Period)
            if board[row][col] == ".":
                # Continue onto the next entry
                continue
        
            # If the entry is in any of the rows, cols, or subgrids
            if (
                board[row][col] in rows[row] or
                board[row][col] in cols[col] or
                board[row][col] in subgrids[(row // 3, col // 3)]):
                # Return False
                return False
            
            # Otherwise, it's not a duplicate and we add that entry to our Hash Sets
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            subgrids[(row // 3, col // 3)].add(board[row][col])
    
    # After iterating if it passes the checks, return true
    return True

"""
R-eview:
    - Looking at NeetCode's solution to this problem, he uses something called
      defaultdict from the collections library. The defaultdict is a subclass
      of the dict from regular Python. It automatically initializes new keys
      with a default value. Which in this case, the default value is an empty
      set.
    - For defaultdict, when trying to access a key that doesn't exist in the
      defaultdict, instead of raising a "KeyError", it automatically creates
      a new entry for that key and initializes it with a default value. 
    - This allows us to directly manipulate the newly created set without
      having to explicitly check if the key exists or create an empty set
      manually.
    - I think that the fact we know the dimensions of the Sudoku board, and
      iterating in range of 9, we can at most make 9 empty sets corresponding
      for each row, col, and subgrid. 
    - In his solution the defaultdicts are obviously used to keep track of the
      numbers we've seen in each row, column, and subgrid in the Sudoku Board
      while we're validating the board.

E-valuate:
    - Considering we have to check over each entry in the Sudoku Board. I think
      the Space Time Complexity is O(9^2). it's 9^2 because we know that the 
      dimensions of the Sudoku Board is set to a 9 x 9 grid. But when 
      considering Complexity, 9^2 is a constant and we can therefore reduce
      it to O(1)
"""

# Testing
# Expects True
board1 = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

# Expects False
board2 = [
["8","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]


print("Board 1: ", isValidSudoku(board1))
print("Board 2: ", isValidSudoku(board2))
