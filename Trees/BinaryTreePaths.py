# LC 257: Binary Tree Paths
# https://leetcode.com/problems/binary-tree-paths/

from typing import List, Optional
from collections import deque

"""
U-nderstand:
     - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is a list of strings that represent all root-to-leaf paths
        in any order.
    - Can the tree be empty?
        No, the number of nodes in the tree range from 1 to 100.

    Happy Case:
    Input: root = [1,2,3,4,5,6,7]
    Output: ["1->2->4", "1->2->5", "1->3->6", "1->3->7]

    Edge Case:
    Input: root = [9]
    Output: ["9"]

M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Using a queue for a Level Order Traversal
        3) Binary Search
        4) Storing in a Hash Map

    For this problem I think we can use a Pre-Order Traversal since we
    want to see every root-to-leaf path, so we'd like to traverse as
    far down as possible first and then check the right subtree path
    if it exist. We can first declare a result and then declare our
    dfs helper function. This will take a node and the current path
    which will be passed an empty string by the outer function and the
    node will be the root. We'll first check if the node doesn't exist,
    if it doesn't, we'd return null. Then we'll check if the node is a
    leaf node, if it is we'll append that value to the current path string
    and append that path to the result list. Then we can recusrively call
    the helper function onto the left and right subtrees. Back in the outer
    function we can call the helper function and return the results list.

P-lan:
    1) Declare our result list
    2) Declare our helper function
    3) Check if the node is null, if so, return null
    4) Check if node is a leaf, if so, append the current path to the result
    5) Recursively call the function on the left and right subtrees
    6) Call the helper function 
    7) Return result list

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Declare our result list
        result = []

        # Create our helper function
        def dfs(node, curr_path):
            # If the node doesn't exist
            if not node:
                # Return null
                return None
            
            # If the node is a leaf, append this current path to the result list
            # Append the value of the node to the end of the current path
            if not node.left and not node.right:
                result.append(curr_path + str(node.val))
                return
            
            # Recusrively Call the function on the left and right subtrees
            # Since it's not a leaf, we know that there must be another node
            # to append, that's why we have the arrow here.
            dfs(node.left, curr_path + str(node.val) + "->")
            dfs(node.right, curr_path + str(node.val) + "->")

        # Call the helper function in the outside function
        dfs(root, "")

        # Return the result list
        return result


    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

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


# Expects ["1->2->4", "1->2->5", "1->3->6", "1->3->7]
node1 = TreeNode(6)
node2 = TreeNode(7)
node3 = TreeNode(3, node1, node2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(2, node4, node5)
tree1 = TreeNode(1, node6, node3)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.binaryTreePaths(tree1), "\n")


# Expects ["9"]
tree1 = TreeNode(9)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.binaryTreePaths(tree1), "\n")


# Expects ["1->2->5", "1->3"]
node1 = TreeNode(5)
node2 = TreeNode(2, None, node1)
node3 = TreeNode(3)
tree1 = TreeNode(1, node2, node3)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.binaryTreePaths(tree1))
