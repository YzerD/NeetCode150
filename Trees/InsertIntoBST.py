# LC 701: Insert Into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input? 
        Our input is the root of a binary search tree (BST) and a value to be
        inserted into the BST.
    - What is our output?
        Our output is the root node of the BST after the insertion
    - Can the value to be inserted be a duplicate?
        No, it is guranteed that the new value doesn't exist in the original BST
    - Can the input tree be empty?
        Yes, the number of nodes in the tree range from 0 to 10^4

M-atch:
    For Trees, common patterns for solutions include:
        1) Storing nodes in a HashMap
        2) Binary Search
        3) Tree Traversal
        4) Level Order Traversal with a queue

        For this problem I think we would have to utilize the strutcture of a BST.
    For a BST, we know that every node to the left of a given node is less than
    it, and every node to the right of a given node is greater than it. So if
    we have the node's value be greater than that of the value to be inserted,
    we know that value to be inserted is less than that node, so it has to be
    inserted somewhere further left. Vice versa for the case if the node's
    value is less than that of the value to be inserted. 
        Base Case should be if the tree is empty, if this is the case we return
    a node with the value to be inserted passed in. We can then check for the
    cases if root's value is less than first, and than the else clause. We can
    set the appropriate child of the root to the recursive call of the function
    to keep checking if we're at the right place. After we've inserted it, we
    return the root node.

P-lan:
    1) Base Case: Check if the tree is empty, return a node with the value to 
       be inserted passed in
    2) Check if the root's value is less than the value to be inserted
    3) If this is the case, we know that the value is greater than the root,
       and should be inserted somewhere further right. Set the root's right
       node to the recursive call with the root.right and val passed in
    4) Otherwise, we know that the root's value is greater than the value
       and we need to set the root's left child to the recursive call with
       the root.left and val passed in
    5) After these calls, we will have successfully inserted the value into
       the BST and should return the root of the BST

I-mplement:
"""

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty
        if not root:
            # Return a tree with a single node with the value passed in
            return TreeNode(val)
        
        # If the root value is less than the value to be inserted
        if root.val < val:
            # We know that the value to be inserted should lay somewhere into the right subtree
            root.right = self.insertIntoBST(root.right, val)
        # Otherwise, we know that root value is greater than the value to be inserted
        else:
            # We know that the value to be inserted should lay somewhere into the left subtree
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the root of the tree after the successful insertion
        return root
    
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

    def display(self, root: Optional[TreeNode], val: int) -> None:
        print(f"Input: root = {self.printLevelOrder(root)}, val = {val}")
        self.insertIntoBST(root, val)
        print(f"Output:       {self.printLevelOrder(root)}\n")


# Testing
solution = Solution()

# Expects [4,2,7,1,3,5]
node1 = TreeNode(1)
node2 = TreeNode(3)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(7)
tree1 = TreeNode(4, node3, node4)
val = 5
solution.display(tree1, val)


# Expects [40,20,60,10,30,50,70,25]
node1 = TreeNode(10)
node2 = TreeNode(30)
node3 = TreeNode(50)
node4 = TreeNode(70)
node5 = TreeNode(20, node1, node2)
node6 = TreeNode(60, node3, node4)
tree1 = TreeNode(40, node5, node6)
val = 25
solution.display(tree1, val)
