# LC 199: Binary Tree Right Side View 
# https://leetcode.com/problems/binary-tree-right-side-view/
# Yzer De Gula 

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is all the values on the right side of the tree
    - Can the tree be empty?
        Yes, the constraints state that the number of nodes in the tree range
        from 0 to 100.

M-atch:
    For trees, common patterns for solutions include:
        1) Binary Search
        2) Tree Traversal
        3) Level Order Traversal with a Queue
        4) Storing in a Hash Map or Set

    Since we have to check level by top to bottom, we can do a level order
    traversal using a queue. This is because at every level the right side
    is the last item at that level.


P-lan:
    1) Check if the tree is empty, if so return an empty list
    2) Declare our result list
    3) Declare our double-ended queue, with the root passed in
    4) While there is something in our queue
    5) Iterating over the current level
    6) Check if the element is the list item in the level
    7) If so, append the item's value to the result list
    8) Check if it has a left child, if so append to queue
    9) Check if it has a right child, if so append to queue
    10) Return result list


I-mplement:
"""
class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the tree is empty
        if not root:
            # If so, return an empty list
            return []
        
        # Declare our result list and our queue with the root passed in
        result, queue = [], deque([root])

        # While there is something in the queue
        while queue:
            # Iterating over the length of the queue
            for i in range(len(queue)):
                # Pop the front of the queue
                node = queue.popleft()

                # If the element is equal to 0
                if i == 0:
                    # Append it to the result list
                    result.append(node.val)

                # If the element has a right child 
                if node.right:
                    # Append it to the queue
                    queue.append(node.right)

                # If the element has a left child
                if node.left:
                    # Append it to the queue
                    queue.append(node.left)

        # Return the result list
        return result


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

# Expects [1,3,4]
node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(2, None, node1)
node4 = TreeNode(3, None, node2)
tree1 = TreeNode(1, node3, node4)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.rightSideView(tree1), "\n")


# Expects [1,3]
node1 = TreeNode(3)
tree1 = TreeNode(1, None, node1)
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.rightSideView(tree1), "\n")


# Expects []
tree1 = None
print("Input:  ", solution.printLevelOrder(tree1))
print("Output: ", solution.rightSideView(tree1))


"""
R-eview:
    - With the first way the logic was implemented the output was actually
      the left side of the tree. So knowing that if we inverted the logic
      len(queue) - 1 to just 0, it returns the right side of the tree.
    - Another thing I had to change was the way we insert the children
      into the queue. Typically, we check left then right, but switching
      it up we can get the right side first.

E-valuate:
    - I think the Time Complexity is O(n) since we're are doing a level
      order traversal, and we're going left to right, level by level
    - I think the Space Complexity is O(n) since we're placing all the
      elements into the queue. 
"""