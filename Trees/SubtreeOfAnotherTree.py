# LC 572: Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
# Yzer De Gula 

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the roots of two binary trees, root and subRoot
    - What is our output?
        Our output is a boolean value that returns truee if there is a subtree
        of root with the same structure and node values of subRoot and false
        otherwise.
    - What is a subtree?
        A subtree of a binary tree is a tree that consists of a node in tree
        and all of this node's descendants. The tree can also be considered
        a subtree of itself.
    - Can the tree's be empty?
        No, The number of nodes in the root tree is 1 to 2000 and the number
        of nodes in the subRoot is 1 to 1000
    - Can the subtree have more nodes than the root tree?
        Yes, There is nothing in the constraints that ensures that the subtree
        has less nodes than the root. 

M-atch:
    - For trees, common patterns for solutions include:
        1) Binary Search
        2) Tree Traversal
        3) Level Order Traversal with a queue
        4) Storing in a Hash Map or Set

    I think for this problem the best option would be traversing the tree in a
    Pre-Order manner. We first wanna check if the subroot doesn't exist, in this
    case we can return True. We can then check if the tree doesn't exist, if it
    doesn't return False. This is because we need the actual tree to exist in
    order to check if the subroot exists. We can also have a helper function
    that checks if both nodes in the root and subtree exist and that they have
    the same value. We can then recursively call the function on the left and
    right subtrees. Then in the outer function we can pass in the root and the
    subroot.
        
P-lan:
    1) Check if the subRoot doesn't exist, if so return True
    2) Check if the Root doesn't exist, if so return False
    3) Declare our helper function that takes in two nodes
    4) Check if both nodes don't exist, if so return True
    5) Then check if both nodes exist and that their values
       are the same
    6) If this is the case, we recursively call the function
       for both the left and right children
    7) Otherwise, they aren't the same and we'd return false
    8) In the outer function return the helper function with
       root and subRoot passed in.


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check if subRoot doesn't exist
        if not subRoot:
            # Return True
            return True

        # Check if root doesn't exist
        if not root:
            # Return False
            return False
        
        # Declare our helper function
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            # If both nodes don't exist
            if not p and not q:
                # Return True
                return True
            
            # Since we know that it exists we can check if both exist and their
            # values are the same
            if (p and q) and (p.val == q.val):
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
            # Otherwise, we know that they aren't the same and we'd return false
            else:
                return False
    
        # If the sub-Tree is the same as the Tree
        if isSameTree(root, subRoot):
            # Return True
            return True
        
        # Otherwise, the sub-Tree might starts somewhere further down the tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    


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
node2 = TreeNode(2)
subtree = TreeNode(4, node1, node2)
node3 = TreeNode(5)
tree1 = TreeNode(3, subtree, node3)
print("Input:   ", solution.printLevelOrder(tree1))
print("subRoot: ", solution.printLevelOrder(subtree))
print("Output:  ", solution.isSubtree(tree1, subtree), "\n")


# Expects False
node1 = TreeNode(1)
node2 = TreeNode(0)
node3 = TreeNode(2, node2)
node4 = TreeNode(4, node1, node3)
node5 = TreeNode(5)
tree1 = TreeNode(3, node4, node5)

node6 = TreeNode(1)
node7 = TreeNode(2)
subtree = TreeNode(4, node6, node7)
print("Input:   ", solution.printLevelOrder(tree1))
print("subRoot: ", solution.printLevelOrder(subtree))
print("Output:  ", solution.isSubtree(tree1, subtree))

"""
R-eview:
    - With the way the logic was first implemented, we were only checking if
      subtree was the same tree. But we can have that check first, and if not
      we can recusrively call the function onto the left and right nodes of the
      root. With that, it functions properly.

E-valuate:
    - The Time Complexity of this function should be O(n^2) since at worst we'd
      have to call the function and the helper n times. 
    - The Space Complexity of this function is O(n) where we'd have n recursive
      calls on the stack. 
"""

