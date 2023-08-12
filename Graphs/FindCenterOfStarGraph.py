# LC 1791: Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

from typing import List

"""
U-nderstand:
  What is input?
    The input is a 2d integer array edges, where each edges[i]  = [ui, vi]
  Is a single node considered a star graph?
    No, the constraints of the problem state the minimum number of nodes n is 3
  What is our output?
    Our output is the center of the given star graph
  What is considered the center?
    The center is the Only node that has more than one edge.
    
M-atch:


P-lan:
Dog is loud
But I think an important thing I noticed is that there is a single common element
in the ui, vi edges

edges = [[1,2],[2,3],[4,2]]
Output = 2

edges = [[1,2],[5,1],[1,3],[1,4]]
Output = 1

I-mplement:
"""

class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    if edges[0][0] in edges[1]:
      return edges[0][0]
    else:
      return edges[0][1]