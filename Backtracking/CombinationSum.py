# LC 39: Combination Sum
# https://leetcode.com/problems/combination-sum/
# Yzer De Gula

from typing import List

"""
U-nderstand:


M-atch:


P-lan:


I-mplement:
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


    def display(self, candidates: List[int], target: int) -> None:
        print(f"Input: candidates = {candidates}, target = {target}")
        print(f"Output: {self.combinationSum(candidates, target)}\n")


# Testing
test = Solution()

# Expects [[2,2,3],[7]]
test.display(candidates = [2,3,6,7], target = 7)

# Expects [[2,2,2,2], [2,3,3], [3,5]]
test.display(candidates = [2,3,5], target = 8)

# Expects []
test.display(candidates = [2], target = 1)