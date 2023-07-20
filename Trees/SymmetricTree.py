# LC 101: Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Yzer De Gula

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is a boolean that is true if the binary tree is a mirror
        of itself, and false otherwise
    - Can the binary tree be empty?
        No, the number of nodes in the tree is in the range of 1 to 1000
    - What does it mean for it to be a mirror of itself?
        The left child of the left subtree is equal to the right child of the
        right subtree. With the right child of the left subtree is equal to the
        left child of the right subtree.

    Happy Case:
    Input: root = [1,2,3,4,5,6,7]
    Output: False

    Input: root = [3,5,5,7,9,9,7]
    Output: True

    Edge Case:
    Input: root = []
    Output: True

    Input: root = [1]
    Output: True

M-atch:
    For Trees, common patterns for solutions include:
        1) Binary Search
        2) Level Order Traversal with a queue
        3) Tree Traversal
        4) Storing nodes in a Hash Map
    
    We don't need Binary Search since we are not searching for anything. Storing
    the nodes in a Hash Map would complicate things, as well as doing a level 
    order traversal. We can do a Pre-Order Traversal to check if the left and right
    subtrees are a mirror. We can first have a base case of if the tree is empty, we
    would return True. We can then have 2 variables that hold the left and right 
    children of the root node. We can then declare our helper dfs function.
    We can first check if both nodes are null, this will be our base case and we'd
    return True. We can then check if both nodes exist and that their values are
    the same. If this is true, we'd recusrively call the function with the left 
    child of left subtree with right child of right subtree, and right child of
    left subtree and left child of right subtree. We'd then return the helper
    function call with the left and right subtrees. This handles the case where
    the tree is empty and has one node. Since if it's empty we'd return True,
    and if there is one node, the left and right vars will be None and in the
    helper function call, we'll return True there since both nodes don't exist.

P-lan:
    1) Check if the tree is empty, if so return True
    2) Declare 2 vars that hold the left and right children of the root
    3) Declare our helper function that takes in two nodes
    4) Check if both nodes are null, if so return True
    5) We can then check if both nodes exist and that their values are
       the same.
    6) If so, we do a recusrive call on the left child of the left subtree
       with the right child of the right subtree. As well as the call on
       the right child of the left subtree and the left child of the right
       subtree. 
    7) We then return the helper function call with the previously saved
       left and right root children nodes.

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Check if tree is empty,
        if not root:
            # If so return True
            return True
        
        # Declare our left and right subtrees
        left = root.left
        right = root.right
        
        # Declare our helper function
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]):
            # Check if both nodes don't exist
            if not left and not right:
                # Return True
                return True
            
            # Check if both nodes exist and have the same value
            if (left and right) and (left.val == right.val):
                # Recurisvely call the function
                return dfs(left.left, right.right) and dfs(left.right, right.left)
            else:
                return False
        
        # Return the call of the helper function
        return dfs(left, right)
    

    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, result = deque([root]), []

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


# Expects True
node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(4)
node5 = TreeNode(3)
node6 = TreeNode(2, node4, node5)
tree1 = TreeNode(1, node3, node6)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isSymmetric(tree1), "\n")


# Expects True
tree1 = None
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isSymmetric(tree1), "\n")


# Expects True
tree1 = TreeNode(1)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isSymmetric(tree1), "\n")


# Expects False
node1 = TreeNode(3)
node2 = TreeNode(2, None, node1)
node3 = TreeNode(3)
node4 = TreeNode(2, None, node3)
tree1 = TreeNode(1, node2, node4)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isSymmetric(tree1))


"""
R-eview:
    - Forgot to include a case where we'd return False, added that after the if
      statement where we check if both nodes exist and have the same value.
"""