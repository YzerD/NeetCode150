# LC 100: Same Tree
# https://leetcode.com/problems/same-tree/
# Yzer De Gula

from typing import List
from typing import Optional

"""
U-nderstand:
    - What is our input?
        Our input is the roots of two binary trees named p and q
    - What is our output?
        Our output is a boolean where we return True if the two trees are the
        same, and false if they are not.
    - What does it mean for binary trees to be considered the same?
        Two binary trees are considered the same if they're structurally
        identical, and the nodes have the same value.
    - Can either or both trees be empty?
        Yes, the constraints state that the number of nodes in both trees range
        from 0 - 100

M-atch:
    For tree questions, common solution patterns include:
        1) Using an appropriate traversal
        2) Using binary search for an element
        3) Storing nodes within a HashMap to refer to later
        4) Apply a level-order traversal with a queue.

    I think for this problem we can use an appropriate traversal so that we can
    check recursively if the left child and right child are the same and then
    work our way up the tree.


    I think the base case should be whether the root nodes don't exist. This is
    because if they both are null, they ended at the same time We can then
    recusively on the left and right subtree to see if they exist and are
    equal, otherwise return false
P-lan:
    1) Check if the root nodes for both trees are null
    2) Check if the values of the nodes are equal
    3) If so, recursively call on the left and right nodes
    4) Otherwise, return false
    

I-mplement:
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both nodes are null (indicates both subtrees have reached the end)
        if not p and not q:
            return True
        # Check if p and q exist and that their values are equal
        if (p and q) and (p.val == q.val):
            # If so, recursively call the function for the left and right nodes
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)
        # Otherwise, they're different and return false
        else:
            return False

solution = Solution()

# Expects True      
node1 = TreeNode(2)
node2 = TreeNode(3)
tree1 = TreeNode(1, node1, node2)
tree2 = TreeNode(1, node1, node2)
print(solution.isSameTree(tree1, tree2))


# Expects True
tree3 = TreeNode()
tree4 = TreeNode()
print(solution.isSameTree(tree3, tree4))


# Expects False
node1 = TreeNode(2)
tree5 = TreeNode(1,node1)
tree6 = TreeNode(1,None,node1)
print(solution.isSameTree(tree5, tree6))

# Expects False
node2 = TreeNode(1)
tree7 = TreeNode(1, node1, node2)
tree8 = TreeNode(1, node2, node1)
print(solution.isSameTree(tree7, tree8))