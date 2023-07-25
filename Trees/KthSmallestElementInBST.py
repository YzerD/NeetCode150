# LC 230: Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a BST 
    - What is our output?
        Our output is the the kth smallest value (1-indexed) of all the
        node in the tree
    - Can our input be empty?
        No, the constraints state that the minimum number of nodes in the tree is 1
    - Can the values in the tree be negative?
        No, the nodes values range from 0 to 10^4
    - Can k be greater than the number of nodes in the tree?
        No, k is less than or equal to the number of nodes in the tree
    - Can there be duplicate values? If so, are they counted in k?
        No, I think due to the nature of a BST duplicates are not allowed.

    
M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Traversal with a queue
        3) Binary Search
        4) Storing in a Hash Map or Set
    
    I think what we can do is get all the nodes in a level order traversal, sort it,
    and return the kth element from that array.
    

P-lan:
    1) Declare our result and dequeue
    2) While there is something in the queue
    3) For the length of the current level
    4) Pop the front of the queue
    5) Append that value to the result list
    6) If the node has a left child, append it to the queue
    7) If the node has a right child, append it to the queue
    8) Sort the result list
    9) Return the kth element from the result list


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Declare our result and dequeue
        result, queue = [], deque([root])

        # While there is something in the queue
        while queue:
            # For the length of the current level
            for i in range(len(queue)):
                # Pop the front of the queue
                node = queue.popleft()

                # Append that value to the result lsit
                result.append(node.val)

                # If the node has a left child, append it to the queue
                if node.left:
                    queue.append(node.left)

                # If the node has a right child, append it to the queue
                if node.right:
                    queue.append(node.right)

        # Sort the result list
        result.sort()

        # Return the k - 1th element of the result list 
        return result[k - 1]
    

    def kthSmallestV2(self, root:Optional[TreeNode], k: int) -> int:
        # Declare our helper function
        def dfs(node):
            # If the tree is empty, return an empty list
            if not node:
                return []
            
            # Declare our result list
            result = []

            # In-Order Traversal goes left subtree, root, then right subtree
            result.extend(dfs(node.left))
            result.append(node.val)
            result.extend(dfs(node.right))

            # Return the result list
            return result
        
        # Return the call of the helper function with the root passed in
        # and return the k-1 value
        return dfs(root)[k - 1]


    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result, queue = [], deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()

                result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
        
        return result
    
    
    def printInOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []

        result.extend(self.printInOrder(root.left))
        result.append(root.val)
        result.extend(self.printInOrder(root.right))

        return result
    
# Testing 
solution = Solution()

# Expects 1
node1 = TreeNode(2)
node2 = TreeNode(1, None, node1)
node3 = TreeNode(4)
tree1 = TreeNode(3, node2, node3)
k = 1
print(f"Input:    {solution.printLevelOrder(tree1)}, k = {k}")
print(f"In-Order: {solution.printInOrder(tree1)}")
print(f"Output:   {solution.kthSmallestV2(tree1, k)} (In-Order)")
print(f"Output:   {solution.kthSmallest(tree1, k)} (Level-Order)\n")


# Expects 3
node1 = TreeNode(1)
node2 = TreeNode(2, node1)
node3 = TreeNode(4)
node4 = TreeNode(3, node2, node3)
node5 = TreeNode(6)
tree1 = TreeNode(5, node4, node5)
k = 3
print(f"Input:    {solution.printLevelOrder(tree1)}, k = {k}")
print(f"In-Order: {solution.printInOrder(tree1)}")
print(f"Output:   {solution.kthSmallestV2(tree1, k)} (In-Order)")
print(f"Output:   {solution.kthSmallest(tree1, k)} (Level-Order)")

"""
R-eview:
    - I'm sure there's a way to optimize this algorithm but this is my naive
      solution.
    - I just modified the printLevelOrder function I've been using for most
      of the tree problems. 
    - While watching the NeetCode solution for a more opimized solution
      Since we know the structure of a BST and that in an In-Order traversal,
      the elements are sorted already. We can reduce the O(nlog(n)) Run Time
      to just O(n). 
    - NeetCode used an iterative implementation, while I did a recusrive one

E-valuate:
    - The Time Complexity is O(nlog(n)) since the highest order in our
      algorithm is the sorting, which is nlog(n)
    - The Space Complexity is O(n) since we put all the nodes of the tree
      into the result list and queue
    - The Level-Order Traversal solution beat 64.45% in Runtime, and only
      51.14% in Memory
    - However, the In-Order solution had the same 64.45% Runtime, but beat
      97.84% in Memory!
"""