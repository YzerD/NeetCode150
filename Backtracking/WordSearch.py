# LC 79: Word Search
# https://leetcode.com/problems/word-search/
# Yzer De Gula

from typing import List

"""
U-nderstand:


M-atch:


P-lan:


I-mplement:
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass


    def display(self, board: List[List[str]], word: str) -> None:
        pass


# Testing
test = Solution()

# Expects True
test.display(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")

# Expects True
test.display(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")

# Expects False
test.display(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")