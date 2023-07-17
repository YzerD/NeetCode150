# LC 94: Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Yzer De Gula

from typing import Optional, List

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is a list of the binary tree that is traversed in inorder 
    - What is inorder?
        Inorder traversal goes through the nodes by going left subtree, root,
        then right subtree
    - Can the binary tree be empty?
        Yes, the constraints state that the number of nodes in the tree range
        from 0 to 100.

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue

    This problem is just an In-Order Traversal, where we first check if the root
    node is null, if so return an empty list. After that we can declare our
    result list and then we can append the recusive call on the left subtree,
    append the root, and then append the right subtree. Where we then return
    the result list

P-lan:
    1) Check if root is null, if so return empty list
    2) Declare our result list
    3) Extend the recusrive call of the left subtree to the result list
    4) Append the root value
    5) Extend the recursive call of the right subtree to the result list
    6) Return the result list


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the root node is null
        if not root:
            return []
        
        # Declare our result list
        result = []

        # In-Order Traversal goes Left Subtree, Root, and then Right Subtere
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))

        # Return the result lsit
        return result
    

# Testing
solution = Solution()

node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(2,node1,node2)
node4 = TreeNode(3)
tree1 = TreeNode(1,node3,node4)

# Expects [4,2,5,1,3]
print("In-Order Traversal:    ", solution.inorderTraversal(tree1))