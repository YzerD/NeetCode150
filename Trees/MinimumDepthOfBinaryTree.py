# LC 111: Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Yzer De Gula 

from typing import Optional

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is an integer representing the minimum depth of the binary 
        tree
    - What is the minimum depth of a binary tree?
        The minimum depth is the number of nodes along the shortest path from
        the root down to the nearest leaf node.
    - What is a leaf node?
        A leaf node is a node with no children.
    - Can the binary tree be empty?
        Yes, The number of nodes in the tree ranges from 0 - 10^5
    
    Happy Case:
    Input: root = [12, null, 3, null, null, null, 4]
    Output: 2

    Input: root = [1, 2, 3, 4, 5, 6, 7, 8]
    Output: 3

    Edge Case:
    Input: root = []
    Output: 0

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue
    
    For this problem, similar to the Maximum Depth we can use a type of tree
    traversal in order to find the Minimum Depth. For this instance, I think
    we can first check if the root is null, this will act as our base case.
    We can then check if both children exist, we can then recursively call
    the function on both subtrees. Then we check if the left child exists,
    and when the right child exists. After that, we know the last case 
    would mean that the node is a leaf node. 

P-lan:
    1) Check if the node is null, if so return 0
    2) Check if both children node exists, if so return the min of the
       recursive call on the subtrees plus 1
    3) Check if the left child node exists, if so return the recursive
       call on the left subtree plus 1
    4) Check if the right child node exists, if so return the recursive
       call on the right subtree plus 1
    5) Otherwise, the node is a leaf since it has not children and we add 1

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the root doesn't exist
        if not root:
            # Return 0
            return 0
        
        # Check if both children exist
        if root.left and root.right:
            # Compare the min of the subtrees and increment the depth
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
        # Check if left child exists
        elif root.left:
            # Recursively call the function on the left subtree and increment the depth
            return self.minDepth(root.left) + 1
        
        # Check if right child exists
        elif root.right:
            # Recursively call the function on the right subtree and increment the depth
            return self.minDepth(root.right) + 1
        
        # Otherwise, the node is a leaf
        else:
            # Increment the depth
            return 1
        
# Testing
solution = Solution()

node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20,node1,node2)
node4 = TreeNode(9)
tree1 = TreeNode(3,node4,node3)

# Expects 2
print("Tree 1: ", solution.minDepth(tree1))

tree2 = None

# Expects 0
print("Tree 2: ", solution.minDepth(tree2))