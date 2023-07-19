# LC 543: Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input? 
        Our input is the root of a binary tree
    - What is our output?
        Our output is the length of the diameter of the tree
    - What is the diameter of a binary tree?
        The diameter of a binary tree is the length of the longest path between
        any two nodes in a tree. This path may or may not pass through the root
    - What the length of a path?
        The length of a path between two nodes is represented by the number of
        edges between them.
    - Can the tree be empty?
        No, the number of nodes in the tree ranges from 1 to 10^4

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue
    
    I think we can do a Pre-Order kind of traversal, where we first check if the
    root is null this will serve as our base case and we'll return 0. Then we have
    to check if the node has both a left and right child, if so, return 1 and the
    max of the recursive call of the subtrees. Then we can check if there only 
    exists a left child, we'd return 1 plus the recursive call for the left
    subtree. Then we can check if only a right child exists, we would then return
    1 plus the recursive call for the right subtree. 

P-lan:
    1) Check if the root is null, if so return 0
    2) Check if the root has both a left and right child
    3) If so, return 1 plus the max of the recursive call of the subtrees
    4) If only a left child exists, return 1 plus the recursive call of the
       left subtree
    5) Otherwise, only a right child exists, return 1 plus the recusrive
       call of the right subtree

I-mplement:
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # BASE CASE: Check if node doesn't exist
        if not root:
            # return 0 if this is the case
            return 0
        
        # Check if node has both left and right children
        if root.left and root.right:
            # Return one plus the max of the recursive call of the subtrees
            return 1 + max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        
        # Check if node has just a left child
        elif root.left:
            return 1 + self.diameterOfBinaryTree(root.left)
        
        # Check if node has just a right child
        else:
            return 1 + self.diameterOfBinaryTree(root.right)
        

    # FROM NEETCODE
    def diameterOfBinaryTreeNeet(self, root: Optional[TreeNode]) -> int:
        # Declare our result variable
        result = 0

        # Create a helper function
        def dfs(root):
            # Use the nonlocal keyword to indicate that the result variable is
            # not local to the helper function but to the outside function
            nonlocal result

            # Base Case: Check if the current node is null
            if not root:
                # If so, return 0
                return 0
            
            # Recursively call the the function to get the heights of the left
            # and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Update the result variable to what is currently stored to the
            # Diameter at this given node
            result = max(result, left + right)

            # Return 1 + the max of the left and right subtrees to get the 
            # height of the current node
            return 1 + max(left, right)
    
        # Call the helper function
        dfs(root)

        # Return diameter of the Binary Tree
        return result


    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # Check if node is null
        if not root:
            # If so return an empty list
            return []
        
        # Declare our result list
        result = []

        # Declare our deque with our root passed in
        queue = deque([root])

        # While there is something in our queue
        while queue:
            # Itearting over the length of the current level
            for i in range(len(queue)):
                # Pop the front of the queue
                node = queue.popleft()

                # Append the value to the result list
                result.append(node.val)

                # If a left child exists
                if node.left:
                    # Append it to the queue
                    queue.append(node.left)
                
                # If a right child exists
                if node.right:
                    # Append it to the queue
                    queue.append(node.right)

                
        # Return result list
        return result
    

# Testing
solution = Solution()

# Expects 3
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(2, node2, node1)
node4 = TreeNode(3)
tree1 = TreeNode(1, node3, node4)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.diameterOfBinaryTree(tree1))
print("Output: ", solution.diameterOfBinaryTreeNeet(tree1), "\n")


# Expects 1
node1 = TreeNode(2)
tree1 = TreeNode(1, node1)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.diameterOfBinaryTree(tree1))
print("Output: ", solution.diameterOfBinaryTreeNeet(tree1))

