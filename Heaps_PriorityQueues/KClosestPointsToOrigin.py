# LC 973: K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Yzer De Gula

from typing import List

"""
U-nderstand:


M-atch:


P-lan:


I-mplement:
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pass


    def display(self, points: List[List[int]], k: int) -> None:
        print(f"Input: points = {points}, k = {k}")
        print(f"Output: {self.kClosest(points, k)}\n")


# Testing
test = Solution()


# Expects [[-2, 2]]
points, k = [[1,3,], [-2,2]], 1
test.display(points, k)

# Expects [[3,3], [-2,4]]
points, k = [[3,3], [5,-1], [-2,4]], 2
test.display(points, k)