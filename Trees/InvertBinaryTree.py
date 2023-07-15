# LC 226: Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is the root node after we've done the inversion
    - What is the inverse of a binary tree?
        The root node stays the same. But the left node of the root gets
        swapped with the right node. 
    - Can the binary tree be empty?
        Yes, in the problem's constraints it states that the number of nodes
        in the tree is in the range 0 - 100.

    Happy Case:
    Input: root = [5,6,7]
    Output: root = [5,7,6]

    Input: root = [1,2,3,4,5,6,7]
    Output: root = [1,3,2,7,6,5,4]

    Edge Case:
    Input: root = []
    Output: root = []

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue
    
    For this problem I think we can use a tree traversal. Specifically, a level
    order traversal. Since we want to check if the root node (subtree) is null,
    this marks the base case. If it exists we perform a swap on the left and 
    right child nodes. After that, we'd recursively call the function on the 
    left and right children. Finally, we'd return the root node. 

P-lan:
    1) Base Case: Check if the root node is null, if it is return null
    2) If it isn't that means it exists and we swap the values of the left and
       right children.
    3) Recursively call the function for the left and right nodes.
    4) Return root node

I-mplement:
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Check if root is null
        if not root:
            return None
        
        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursively call the function on the roots children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the root
        return root
    
    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If root is null, return an empty list
        if not root:
            return []

        # Declare our result list
        result = []
        queue = deque([root])  # Use a deque as a queue for level-order traversal
        
        while queue:
            node = queue.popleft()  # Remove the first node from the queue
            
            result.append(node.val)  # Append the node value to the result list
            
            if node.left:
                queue.append(node.left)  # Add the left child to the queue
                
            if node.right:
                queue.append(node.right)  # Add the right child to the queue

        # Return Result List
        return result
    
# Testing 
solution = Solution()

# Expects [2,3,1]
node1 = TreeNode(1)
node2 = TreeNode(3)
tree1 = TreeNode(2,node1,node2)
print("Tree 1 Before Inversion: ", solution.printLevelOrder(tree1))
solution.invertTree(tree1)
print("Tree 1 After Inversion:  ", solution.printLevelOrder(tree1))

# Expects [4,7,2,9,6,3,1]
solution.invertTree(tree1)
node3 = TreeNode(6)
node4 = TreeNode(9)
tree2 = TreeNode(7, node3, node4)
tree3 = TreeNode(4, tree1, tree2)
print("Tree 2 Before Inversion: ", solution.printLevelOrder(tree3))
solution.invertTree(tree3)
print("Tree 2 After Inversion:  ", solution.printLevelOrder(tree3))

# Expects [None]
tree4 = TreeNode(None)
print("Tree 3 Before Inversion: ", solution.printLevelOrder(tree4))
solution.invertTree(tree4)
print("Tree 3 After Inversion:  ", solution.printLevelOrder(tree4))

