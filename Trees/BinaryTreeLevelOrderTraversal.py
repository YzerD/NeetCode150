# LC 102: Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Yzer De Gula

from typing import List, Optional
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is a list of lists that represent the level order traversal
        of the given Binary Tree
    - What is Level Order Traversal?
        Level Order Traversal goes through the nodes from left to right, level
        by level.
    - Can the binary tree be empty?
        Yes, the number of nodes can range from 0 to 2000

    Happy Case:
    Input: root = [1,2,3,4,5,6,7]
    Output: [[1],[2,3],[4,5,6,7]]

    Input: root = [7,null,5,null,null,10,11]
    Output: [[7],[5],[10,11]]

    Edge Case:
    Input: root = []
    Outpuit: []

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue
    
    For this problem we'd have to do a level-order traversal with a queue.
    For this, we need to have a dequeue from the collections library and
    we need to check if the node exists first, we would return an empty
    list if it is. We can then declare our result list and our deque with
    the root passed in. Then while there is something in our queue, we can
    declare another list which will be for the current level. Then for the
    range of whatever is in the queue (This is iterating over whatever nodes
    are in the queue for the current level) we would pop the front element,
    append that value to the current level list, and check if a left or
    right child exists, if so append them to the queue. After we iterate
    over the current level, append that list to the result list. Finally,
    we would return the result list.

P-lan:
    1) Check if the root is null, if so return an empty list
    2) Declare our result list 
    3) Declare our deque and pass in the root
    4) While there is something in the queue
    5) Declare our current level list
    6) For the length of the current level (Whatever is in the queue)
    7) Pop the front of the queue and store it into a temp var, node
    8) Append that value to the current level list
    9) Check if a left child exists, if so append it to queue
    10) Check if a right child exists, if so append it to the queue
    11) Append the current level list to the result list
    12) Return result list

I-mplement:
"""

class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Check if root is null
        if not root:
            # If so, return an empty list
            return []
        
        # Declare our result list
        result = []

        # Declare our dequeue with root passed in
        queue = deque([root])

        # While there is something in the queue
        while queue:
            # Declare a current level list
            current_level = []

            # Iterating over the length of the level
            for i in range(len(queue)):
                # Pop the front element
                node = queue.popleft()

                # Append that value to the current level list
                current_level.append(node.val)

                # If a left child exists
                if node.left:
                    # Append it to the queue
                    queue.append(node.left)
                
                # If a right child exists
                if node.right:
                    queue.append(node.right)
            
            # Append current level list to result list
            result.append(current_level)

        # Return result list
        return result
            
# Testing
solution = Solution()

# Expects [[1],[2,3],[4,5,6,7]]
node1 = TreeNode(6)
node2 = TreeNode(7)
node3 = TreeNode(3,node1,node2)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(2,node4,node5)
tree1 = TreeNode(1,node6,node3)
print(solution.levelOrder(tree1))

print("\n")

# Expects []
tree2 = None
print(solution.levelOrder(tree2))

print("\n")

# Expects [[7],[5],[10,11]]
node1 = TreeNode(11)
node2 = TreeNode(10)
node3 = TreeNode(5,node2,node1)
tree3 = TreeNode(7,None,node3)
print(solution.levelOrder(tree3))