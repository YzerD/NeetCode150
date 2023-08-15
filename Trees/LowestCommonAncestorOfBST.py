# LC 235: Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a BST, and two nodes p and q that we have to
        find the Lowest Common Ancestor of.
    - What is the Lowest Common Ancestor (LCA)?
        The LCA is defined between two nodes p and q as the lowest node in T
        that has both p and q as descendants (where we allow a node to be a
        descendant of itself)
    - What is our output?
        Our output is a TreeNode that is the LCA of nodes p and q
    - Can our tree be empty?
        No, the number of nodes in the tree is in the range of 2 to 10^5
    - Can p and q be the same node?
        No, the constraints state that p != q
    - Can the values of p and q be the same?
        No, the constraints state that all nodes in the BST are unique
    - Does a solution always exist?
        Yes, the constraints state that p and q will exist in the BST

M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Traversal with a queue
        3) Binary Search
        4) Storing in a Hash Map or Set
    
    We can probably traverse the tree in a Pre-Order traversal to check if the
    node doesn't exist, if it doesn't return None. Then we can check if the
    node is both greater than the values of p and q. If so, we know that the
    LCA lies somewhere further down the left subtree. Then in the case where
    the current node has a lesser value than that of p and q we know that it
    lies somewhere down the right subtree. Otherwise we can return the node.

P-lan:
    1) Check if node doesn't exist, if so return None
    2) Check if the current node is greater than both p and q
    3) If so, recusrively call the function down the left subtree
    4) Otherwise, check if the current node is lesser than both p and q
    5) If so, recursively call the function down the right subtree
    6) Otherwise, we are at the LCA and we return that value. 

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Check if node is null
        if not root:
            return None
        
        # Check if node is greater than both p and q
        if (root.val > p.val) and (root.val > q.val):
            # Recursive call down the left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        
        # Check if node is lesser than both p and q
        elif (root.val < p.val) and (root.val < q.val):
            # Recursive call down the right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        
        # Otherwise, we're at the LCA
        else:
            # Return the node's value
            return root.val
        

    def lowestCommonAncestorLC(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Set a variable to the root node
        curr = root

        # While there is still something in our tree
        while curr:
            # Check if root is greater than both p and q
            if (curr.val > p.val) and (curr.val > q.val):
                # Set the current node to the left child
                curr = curr.left
            # Check if root is lesser than both p and q
            elif (curr.val < p.val) and (curr.val < q.val):
                # Set the current node to the right child
                curr = curr.right
            # Otherwise, we're at the LCA
            else:
                # Return the node's value
                return curr

    
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
    
# Testing 
solution = Solution()

node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(4, node1, node2)
node4 = TreeNode(0)
node5 = TreeNode(2, node4, node3)
node6 = TreeNode(7)
node7 = TreeNode(9)
node8 = TreeNode(8, node6, node7)
tree1 = TreeNode(6, node5, node8)
p = TreeNode(2)
q = TreeNode(8)

# Expects 6
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.lowestCommonAncestor(tree1, p, q))


# Expects 2
p = TreeNode(2)
q = TreeNode(4)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.lowestCommonAncestor(tree1, p, q))