# LC 98: Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is a boolean that returns true if the binary search tree is
        a valid BST
    - What is a BST?
        A valid BST has the left subtree of a node contain only nodes with keys
        less than the node's key. The right subtree of a node contains only
        nodes with keys greater than the node's key. Finally, both the left
        and right subtrees must also be binary serach tree.
    - Can the input be empty?
        No, the constraints state that the number of nodes in the tree range
        from 1 to 10^4. 

M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Traversal with a queue
        3) Binary Search
        4) Storing in a Hash Map or Set

    For this problem we can traverse through the tree in a Pre-Order traversal,
    We first want to check if the node is null, if it is return True. Then 
    since we know that it exists, we can check if the node to the left is less
    than the node and that the right to the right is greater than the node. 
    

P-lan:
    1) Check if the node is null, if so return True
    2) Then since we know the node exists, we can check if a left child exists
       and that the value of it is less than the current node
    3) We can then recursively call the function on the left child
    4) We can then check if a right child exists, and that its value is greater
       than that of the node
    5) We then recursively call the function on the right child
    6) Otherwise, the BST doens't hold and we return false. 

I-mplement:
"""
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Declare our helper function
        def helper(node, left=float('-inf'), right=float('inf')):
            # First check if tree is empty
            if not node:
                # Return true because an empty tree is a valid BST
                return True
            
            # Check if the inequality doesn't hold
            if not (left < node.val < right):
                return False
            
            # Otherwise, return the recursive call for both left and right subtrees
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
    
        # Call the helper function with the root passed in
        return helper(root)


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


# Expects True
node1 = TreeNode(1)
node2 = TreeNode(3)
tree1 = TreeNode(2, node1, node2)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isValidBST(tree1))


# Expects False
node1 = TreeNode(3)
node2 = TreeNode(6)
node3 = TreeNode(4, node1, node2)
node4 = TreeNode(1)
tree1 = TreeNode(5, node4, node3)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.isValidBST(tree1))

"""
R-eview:
    - NeetCode Video Solution: https://www.youtube.com/watch?v=s6ATEkipzow
    - After trying to naively solve this problem, I was getting unexpected
      results back from the test cases. I then watched the video solution
      of this problem on NeetCode's Youtube. We can take advantage of the 
      fact that for the root node, it doesn't matter what the value is. So
      we can have a helper function that has lower and upper limits to
      infinity. The helper first check if the node exists, if not we return
      true. Then we check if the inequality holds for the root (which it 
      always will, -inf < root.val < inf) and we would then do the
      recursive calls on the left and right subtrees while updating the limits.
    - For the left subtree we'd have to update the right limit to check if the
      value is less than its parent node.
    - For the right subtree we'd have to update the left limit to check if the
      value is greater than its parent node.


E-valuate:
    - The Space Time Complexity of this function is both O(n) since we'd have
      to traverse all the nodes in order to determine if the binary tree is a
      valid BST. The Space is O(n) because in the worst case we'd have n 
      recusrive calls onto the stack.
"""
