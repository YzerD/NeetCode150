# LC 74: Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an m x n integer matrix, named matrix with the two 
        following properties:
        1) Each row is sorted in non-decreasing order
        2) The first integer of each row is greater than the last integer
           of the previous row.
    - What is our output?
        Our output is a boolean that returns true if the target is found
        within the matrix, and false otherwise.
    - Are there any restrictions on memory or runtime?
        Yes, the problem specifies that the solution must be O(log(m * n)) time
    - Can our input matrix be empty?
        No, the minimum dimensions our input matrix can be is 1 x 1.
    
M-atch:
        Considering that the problem specifies that the runtime of our solution
    be O(log(m * n)) and the nature of our input matrix, we have to use binary 
    search. I think similar to Spiral Matrix and Rotate Image we can utilize
    four pointers: left, right, top, and bottom. We can first perform binary
    search on the first entry of the rows in our matrix. While our top and
    bottom pointers haven't crossed, if matrix[left][middle] == target, return
    true. Then we can check if matrix[left][middle] < target, if this is the
    case.

        I think we need to change the logic for determining which row to 
    perform the binary search in. Initially, I thought of checking only the 
    first element of a row but that only check one end of the range in a row.
    I also think that we shouldn't check if the element is equal to the target
    we'll just leave that to the binary search within the row. So we first have
    to calculate the middle row and that is top + bottom // 2. We can then check
    if the first element of the row is greater than the target, and if so, this 
    means that the target lies within a row with lesser values, that being 
    in a lesser row index, so we'd set bottom = middle_row + 1. Then we can
    check if the last element in a row is less than the target. If this is true
    then we know that the target lies in a higher row index since every row in
    a higher row index consists of greater values. Otherwise, we'd break out
    of this loop since we've found the row we need to do the binary search in.
    Then in the case where we've searched through all the rows we can return
    false. We can then perform the binary search algorithm at that row. 

P-lan:
    1) Get the dimensions of our matrix
    2) Declare our top and bottom pointers
    3) While our top and bottom pointers haven't met
    Calculate our middle row
    4) If first element in the row is greater than the target
    5) We know that the target lies in a lesser row index since lesser values
       occupy the lower row indicies, and we update our bottom pointer
    6) If the last element in the row is lesser than the target
    7) We know that the target lies in a greater row index since greater values
       occupy the higher row indicies, and we update our top pointer
    8) Otherwise, we know that the target is in that row and we break out of 
       the loop
    9) If none of the rows contain the target value, we return false.
    10) Since we've found the row we calculate it again with our updated top
        and bottom pointers.
    11) Declare our left and right pointers
    12) While our left and right pointers haven't crossed
    13) Calculate the middle index 
    14) If middle is equal to target, return True
    15) If middle is less than target, update our left pointer
    16) If middle is greater than target, update our right pointer
    17) If after we've done this, we can return False.

I-mplement:
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the dimensions of the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Declare our top and bottom pointers
        top, bottom = 0, ROWS - 1

        # While our top and bottom pointers haven't met
        while top <= bottom:
            # Calculate middle row 
            middle_row = (top + bottom) // 2

            # Check if first element in the row is greater than the target
            if matrix[middle_row][0] > target:
                # We know that the target lies in a lower row and we update our bottom pointer
                bottom = middle_row - 1

            # Check if last element in the row is less than the target
            elif matrix[middle_row][-1] < target:
                # We know that the target lies in a higher row and we update our top pointer
                top = middle_row + 1
            
            # Otherwise, we know that we're in the right row
            else:
                break
        
        # If after checking all the rows and none of them contain the target value
        if not (top <= bottom):
            # We return False
            return False
        
        # Since we know the row to search we can perform the binary search
        middle_row = (top + bottom) // 2

        # Declare our left and right pointers
        left, right = 0, COLS - 1

        # While our two pointers haven't crossed
        while left <= right:
            # Calculate middle index
            middle = (left + right) // 2

            # If the middle index is greater than the target
            if matrix[middle_row][middle] > target:
                # So we update our right pointer
                right = middle - 1
            
            # If the middle index is less than the target
            elif matrix[middle_row][middle] < target:
                # We know that the target lies somewhere further right
                left = middle + 1
            
            # Otherwise the middle index is equal to the target
            else:
                # Return True
                return True
            
        # Return False as the default return value
        return False


    def display(self, matrix: List[List[int]], target: int) -> None:
        print(f"Input: matrix = {matrix}")
        print(f"Output:         {self.searchMatrix(matrix, target)}\n")


# Testing
solution = Solution()


# Expects True
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution.display(matrix, target)

# Expects False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
solution.display(matrix, target)


"""
R-eview:
    - Had to watch video solution from NeetCode in order to figure out how
    to properly find the row we must perform the binary search on. The 4 
    pointers were present. But I think just keeping track of all of them
    can get confusing. But It's binary search with a slight twist, I had
    to draw out how the calculation of the row to perform binary search
    worked. It makes sense now, which is good. 

E-valuate:
    - As per the specifications of the problem, this solution runs at 
    O(log(n * m)) time and has a Space Complexity of O(1) since we only
    used 4 pointers and no auxilary data structure.
"""