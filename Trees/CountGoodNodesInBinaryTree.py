# LC 1448: Count Good Nodes in Binary Tree
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is the number of good nodes in the binary tree
    - What is considered a good node?
        A good node if in the path from root to X there are no node with
        a value greater than X.
    - Can the input binary tree be empty?
        No, In the constraints the number of nodes in the binary tree is in
        the range 1 to 10^5
    
    Happy Case:
    Input: root = [1,2,3,4,5,6,7]
    Output: 7

    Input: root = [2,1,3,None,None,-4,-7]
    Output: 2 

    Edge Case:
    Input: root = [3]
    Output: root = 1



M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Traversal with a queue
        3) Binary Search
        4) Storing in a Hash Map or Set
    
    For this problem I think a Pre-Order Tree Traversal is the most valid
    approach to solving this. This is because the minimum number of nodes
    in the input binary tree is 1, meaning we have to consider the case
    where it is just the root node. The root node has no leafs but there
    is no node with a value greater than itself, making it a good node.
    We would then have to traverse the left subtree and the right subtree
    and calculate the amount of good nodes by comparing the child node
    to the parent node and getting the max of it. We're gonna need a helper
    function since we need to traverse both subtree and keep track of a max
    value. 

P-lan:
    1) Declare our helper function that takes in a node and a max value
    2) If the node doesn't exist, we return 0, since it's not a good node
    3) Since we know it exists, if its value is greater than the max, it's
       considered a good node and we'd set a result or counter variable to 1.
    4) Otherwise, the node is not a good node and we'd set it to 0
    5) We'd then get our new max by comparing the currently held max value and
       the node's value
    6) We'd then add the recursive call of the left and subtree to our counter
    7) Return the counter
    8) In the outer function, return the call of the helper function with the
       root and the root's value passed in.


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Declare our helper function
        def helper(node, max_val):
            # Check if the node doesn't exist
            if not node:
                # Return 0, since it's not considered a good node
                return 0
            
            # Update our max variable
            max_val = max(max_val, node.val)
            
            # Since we know it exists, check if it's value is greater than that
            # of the currently held max value
            if (node.val >= max_val):
                good_nodes = 1
            # Otherwise, it's not a good node
            else:
                good_nodes = 0
        

            # Add the recursive calls of the node's subtrees
            good_nodes += helper(node.left, max_val)
            good_nodes += helper(node.right, max_val)

            # Return the number of good nodes 
            return good_nodes

        # Return the helper function with the root and its value passed in
        return helper(root, root.val)

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
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
# Testing 
solution = Solution()

# Expects 4
node1 = TreeNode(3)
node2 = TreeNode(1, node1)
node3 = TreeNode(1)
node4 = TreeNode(5)
node5 = TreeNode(4, node3, node4)
tree1 = TreeNode(3, node2, node5)
print("Input:     ", solution.printLevelOrder(tree1))
print("Output:    ", solution.goodNodes(tree1), "\n")


# Expects 7
node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(6)
node4 = TreeNode(7)
node5 = TreeNode(2, node1, node2)
node6 = TreeNode(3, node3, node4)
tree1 = TreeNode(1, node5, node6)
print("Input:     ", solution.printLevelOrder(tree1))
print("Output:    ", solution.goodNodes(tree1), "\n")


# Expects 2
node1 = TreeNode(-4)
node2 = TreeNode(-7)
node3 = TreeNode(1)
node4 = TreeNode(3, node1, node2)
tree1 = TreeNode(2, node3, node4)
print("Input:     ", solution.printLevelOrder(tree1))
print("Output:    ", solution.goodNodes(tree1), "\n")


# Expects 3
node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(3, node1, node2)
tree1 = TreeNode(3, node3)
print("Input:     ", solution.printLevelOrder(tree1))
print("Output:    ", solution.goodNodes(tree1))
