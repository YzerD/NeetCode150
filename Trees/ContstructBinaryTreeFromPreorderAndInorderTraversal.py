# LC 105: Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is two integer arrays that represent the preorder and inorder
        traversals of the binary tree we are meant to build
    - What is our output?
        Our output is the root of constructed binary tree
    - Can the input be empty?
        No, the lengths of the input array have a minimum of 1
    - Can the input arrays be of differing lengths?
        No, the length of the input arrays are of the same length
    - What is the difference between Preorder and Inorder Traversal?
        Preorder traversal starts at the root, left subtree, and then the right
        subtree. Inorder Traversal goes left subtree, root, then right subtree.

    Happy Case:
    Input: preorder = [1,2,4,5,3], inorder = [4,2,5,1,3]
    Output: [1,2,3,4,5]

    Edge Case:
    Input: preorder = [9], inorder = [9]
    Output: [9]

M-atch:
    For Trees, common patterns for solutions include:
        1) Tree Traversal
        2) Level Order Traversal with a queue
        3) Binary Search
        4) Storing in a Hash Map or Set
    
    For this problem we first have to check if either input array doesn't exist.
    If this is the case, we return null. But since we know that they're both the
    same length, we only need to check if one of the input arrays are empty.
    From then on we need to create our tree. Knowing that we are dealing with
    a Preorder and Inorder array representation of the tree we are meant to 
    construct, we can see that the first element of the preorder is always the
    root node. From there we can take the value of the root and find the index
    of where it's located in the inorder array, this is because everything to
    the left of that index is in the left subtree and everything to the right
    is in the right subtree. We can then set the root's left and right children
    to the recursive call of the function with the input arrays sliced 
    accordingly. For the root's left child, we need to slice the next index
    which is 1 all the way up to the middle index plus 1. It's plus 1 since
    we know that in Python the end is non-inclusive so when we add the plus 1
    we can include mid. The inorder array is sliced by having everything in the
    beginning up to the middle index (not-including) since we don't want to
    include the root value again. The call for the root's right child is the
    opposite of the left, it should be mid + 1 up to the end. This is because
    the start point IS inclusive and want to include the value beyond the root.

P-lan:
    1) Check if one of the input arrays are empty
    2) Declare the root node with its value being the first element in the
       Preorder array
    3) Calculate the index of the root's value in the inorder array
    4) Set the root's left child to the recursive call of the function
    5) Set the root's right child to the recursive call of the function
    6) Return the root


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Check if the input array is empty
        if not preorder or not inorder:
            # Return null
            return None
        
        # Create the root node
        root = TreeNode(preorder[0])

        # Get the index of the root's value in the inorder array
        middle = inorder.index(root.val)

        # Create the root's left node by the recursive call of the function
        root.left  = self.buildTree(preorder[1:middle + 1], inorder[:middle])

        # Create the root's right node by the recursive call of the function
        root.right = self.buildTree(preorder[middle + 1:], inorder[middle + 1:])

        # Return the root of the newly constructed tree
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
    

    def display(self, preorder: List[int], inorder: List[int]):
        print(f"Input:  preorder = {preorder}, inorder = {inorder}")
        print(f"Output: {self.printLevelOrder(self.buildTree(preorder, inorder))}\n")
        
    
# Testing 
solution = Solution()

# Expects [3,9,20,15,7]
preorder = [3,9,20,15,7]
inorder  = [9,3,15,20,7]
solution.display(preorder, inorder)


# Expects [1,2,3,4,5]
preorder = [1,2,4,5,3]
inorder  = [4,2,5,1,3]
solution.display(preorder, inorder)
