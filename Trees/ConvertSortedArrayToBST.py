# LC 108: Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is an integer array where the elements are stored in
        ascending order
    - What is our output?
        Our output is the root of the height-balanced binary search tree
    - What is a height-balanced BST?
        A height-balanced binary tree is a binary tree in which the depth
        of the two subtrees of every node never differs by more than one.
    - Can the input array be empty?
        No, the problem's constraints state that the length of the array
        ranges from 1 - 10^4.
    
    Happy Case:
    Input: nums = [1,3,5]
    Output: [3,1,5]

    Input: nums = [3,5,7,9,11]
    Output: [7,3,9,5,11]

    Edge Case:
    Input: nums = [9]
    Output: [9]

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue

    I think for this problem, we can use the fact that the input
    array is sorted to our advantage. For BST's we know that everything
    to the left of a node is lesser than that, and everything to the right
    of the node is greater than that node. Our base case should be when
    the input array is exhausted, or when it equals 0. We can then set
    the root to middle, and then recursively call the function while
    updating the location of the middle pointer. The left subtree
    would get the input array sliced from the beginning up to the middle,
    since we know that the end point is not inclusive. Then we can call
    the function on the right subtree with the updated parameter being
    middle + 1 to the end. We would then return the root of the tree.
    
P-lan:
    1) Base Case: Check if the input array is 0, return null
    2) Calculate the middle index of the length of the array
    3) Make a TreeNode with it's value from the middle index
    4) Recusrively call the function for the left child from the
       beginning up to the middle
    5) Recusrively call the function for the right child the middle + 1
       to the end of the array
    6) Return the root of the new tree


I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # BASE CASE: Check if input array is empty
        if (len(nums) == 0):
            return None
        
        # Calculate the middle index
        middle = len(nums) // 2

        # Create a root node with the value of that middle index
        root = TreeNode(nums[middle])

        # Create the children with recusrive calls
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])

        # Return the root of the newly constructed tree
        return root
    
    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # Check if root is null
        if not root:
            # If so, return an empty list
            return []
        
        # Declare our result list
        result = []

        # Declare our deque
        queue = deque([root])

        # While there is something in the queue
        while queue:
            # For the length of the current level
            for i in range(len(queue)):
                # Remove the front node
                node = queue.popleft()

                # Append that value to the result list
                result.append(node.val)

                # If a left child exists
                if node.left:
                    # Append it to the queue
                    queue.append(node.left)
                
                # If a right child exists
                if node.right:
                    # Append it to the queue
                    queue.append(node.right)
            
        # Return the result list
        return result
    

# Testing
solution = Solution()

# Expects [0,-3,9,-10,5]
nums1 = [-10,-3,0,5,9]
tree1 = solution.sortedArrayToBST(nums1)
print("Input Array: ", nums1)
print("BST:         ", solution.printLevelOrder(tree1))

print("\n")

# Expects [3,1,5]
nums2 = [1,3,5]
tree2 = solution.sortedArrayToBST(nums2)
print("Input Array: ", nums2)
print("BST:         ", solution.printLevelOrder(tree2))

print("\n")

# Expects [9]
nums3 = [9]
tree3 = solution.sortedArrayToBST(nums3)
print("Input Array: ", nums3)
print("BST:         ", solution.printLevelOrder(tree3))

print("\n")

# Expects [3,1]
nums4 = [1,3]
tree4 = solution.sortedArrayToBST(nums4)
print("Input Array: ", nums4)
print("BST:         ", solution.printLevelOrder(tree4))

