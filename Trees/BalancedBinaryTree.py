# LC 110: Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output? 
        Our output is a boolean that returns true if it's height-balanced,
        false otherwise
    - What is height-balanced?
        Height-balanced binary tree is a binary tree in which the depth of the
        two subtrees of every node never differs by more than one. 
    - Can the input tree be empty?
        Yes, the number of nodes in the tree ranges from to 0 to 5000.
    - What is the difference between height and depth?
        Height of a node is the number of edges on the longest path from the
        node to a leaf. While depth of a node is the number of edges from the
        node to the tree's root.
    
    Happy Case:
    Input: root = [1,2,3,4,5]
    Output: True

    Input: root = [1,2,null,3,4]
    Output: False

    Edge Case:
    Input: root = []
    Output: False

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue

    I think for this problem, we can use a Pre-Order Traversal which is a type
    of DFS since we want to figure out the heights of the subtrees and see if
    they differ by one. So we'd like to traverse as far down as we can and then
    compare. 

P-lan:
    1) Base Case: Check if tree exists, an empty tree is balanced
    2) Declare our helper function from Max Depth of a Binary Tree LC problem
    3) Return the absolute value of the difference of the subtrees and see if
       it's less than or equal to 1. Also check if the left and right subtrees
       are balanced as well.

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Check if the tree is empty
        if not root:
            # Return True since an empty tree is a balanced one
            return True

        # Use the DFS solution of Max Depth
        def height(node):
            # Check if node is null
            if not node:
                # If so, return 0
                return 0
            
            # Otherwise increment the depth and take the max of the left and right subtrees 
            return 1 + max(height(node.left), height(node.right))

        # Return the absolute value of the heights of the subtrees, and if the left and right subtrees are balanced as well
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    

    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # Check if tree is empty
        if not root:
            # If so, return an empty list
            return []
        
        # Declare our queue and result list
        result = []
        queue = deque([root])

        # While there is something in the queue
        while queue:
            # Iterating over the length of the current level
            for i in range(len(queue)):
                # Pop the front of the queue
                node = queue.popleft()

                # Append the value to the result list
                result.append(node.val)

                # Check if a left child exists
                if node.left:
                    queue.append(node.left)

                # Check if a right child exists
                if node.right:
                    queue.append(node.right)
                
        # Return result list
        return result
    

# Testing
solution = Solution()


# Expects True
node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
tree1 = TreeNode(3, node4, node3)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isBalanced(tree1), "\n")


# Expects False
node1 = TreeNode(4)
node2 = TreeNode(4)
node3 = TreeNode(3, node1, node2)
node4 = TreeNode(3)
node5 = TreeNode(2, node3, node4)
node6 = TreeNode(2)
tree1 = TreeNode(1, node5, node6)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isBalanced(tree1), "\n")


# Expects True
tree1 = None
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isBalanced(tree1))

        
        