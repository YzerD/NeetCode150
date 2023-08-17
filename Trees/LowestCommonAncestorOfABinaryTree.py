# LC 236: Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Yzer De Gula

"""
U-nderstand:
    # ? What is our input ?
        Our input is a binary tree
    # ? What is our output ?
        Our output is the lowest common ancestor of the two nodes
    # ? What does lowest common ancestor mean ?
        The lowest common ancestor is the lowest node that has both nodes as descendants
    # ? What if one of the nodes is the ancestor of the other ?
        Then the ancestor is the lowest common ancestor
    # ? What if one of the nodes is not in the tree ?
        Then return None
    # ? What if the tree is empty ?
        Then return None


M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Tree Traversal with Queue
        3) Storing in a Hash Map or Set
        4) Binary Search

    For this problem, doing a level order traversal will complicate our code.
    We don't need to store the nodes in a hash map or set. We aren't working
    with a binary search tree, so we can't use binary search. That leaves us
    with using a tree traversal. More specifically a post-order traversal.
    This is because we want to visit the left and right nodes first before
    visiting the root node. This will allow us to check if the left and right
    nodes are descendants of the root node. If they are, then we can return
    the root node. If not, then we can return None.

P-lan:
    1) Check if the root node is None
        a) If it is, then return None
    2) Check if the root node is equal to either p or q 
        a) If it is, then return the root node
    3) Recursively call the function on the left and right nodes
        a) If the left node is None, then return the right node
        b) If the right node is None, then return the left node
        c) If both nodes are not None, then return the root node
    4) If the left and right nodes are None, then return None

I-mplement:
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check if the root node is None
        if root is None:
            return None
        
        # Check if the root node is equal to either p or q
        if root == p or root == q:
            return root
        
        # Recursively call the function on the left and right nodes
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p ,q)

        # If the left node is None, then return the right node
        if left is None:
            return right
        
        # If the right node is None, then return the left node
        if right is None:
            return left
        
        # If both nodes are not None, then return the root node
        if left is not None and right is not None:
            return root


# Testing 
test = Solution()

# Expects 3
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


print(test.lowestCommonAncestor(root, 5, 1)) # 3


# Expects 5
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)


print(test.lowestCommonAncestor(root, 5, 4)) # 5

