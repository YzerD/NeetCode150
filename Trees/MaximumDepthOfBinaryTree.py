# LC 104: Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Yzer De Gula

from typing import Optional, List
from collections import deque

"""
U-nderstand:
    - What is our input?
        Our input is the root of a binary tree
    - What is our output?
        Our output is the tree's maximum depth
    - What is the maximum depth of a binary tree?
        The maximum depth is the number of nodes along the longest path from
        the root node down to the farthest leaf node.
    - Can the binary tree be empty?
        Yes, in the constraints the problem states that the number of nodes
        in the tree is in the range 0 - 10^4. 

    Happy Case:
    Input: root = [7,6,8,null,15,null,18,3]
    Output: 3

    Input: root = [1,2,3,4,null]
    Output: 3

    Edge Case:
    Input: root = []
    Output: 0

M-atch:
    For Tree problems, common patterns for solutions include:
        1) Tree Traversal
        2) Store nodes within a HashMap to refer to later
        3) Using Binary Search to find an element
        4) Applying a level-order traversal with a queue

    For this problem, I think Tree Traversal would be the best choice for
    finding the solution. We can declare a counter for the depth, and then
    check if the root node is null. This will act as our base case, since
    if there is no node whatever depth we're at is the max we can go. 
    Therefore we would return our depth counter. After this we can
    call the function on the left and right children. 

P-lan:
    1) Declare our depth counter
    2) Check if the node is null. If so, return depth
    3) Recursively call the function onto the left and right children

I-mplement:
"""
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recursive DFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Check if root is null
        if not root:
            # If so, return 0
            return 0
        
        # Otherwise increment the depth and take the max of the left and right subtrees 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    

    # BFS 
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # Declare our dequeue
        queue = deque()

        # If the root exists
        if root:
            # Append that to the queue
            queue.append(root)

        # Declare our depth counter
        level = 0

        # While there is something in our queue
        while queue:
            # Iterating over the length of the queue
            for i in range(len(queue)):
                # Set a node to the front of the queue
                node = queue.popleft()
                # If a left child exists
                if node.left:
                    # Append it to the end of the queue
                    queue.append(node.left)
                # If a right child exists
                if node.right:
                    # Append it to the end of the queue
                    queue.append(node.right)
            # Increment depth counter
            level += 1
        # Return depth counter
        return level
    

    def printLevelOrder(self, root: Optional[TreeNode]) -> List[int]:
        # If root is null, return an empty list
        if not root:
            return []

        # Declare our result list
        result = []
        queue = deque([root])  # Use a deque as a queue for level-order traversal
        
        while queue:
            node = queue.popleft()  # Remove the first node from the queue
            
            result.append(node.val)  # Append the node value to the result list
            
            if node.left:
                queue.append(node.left)  # Add the left child to the queue
                
            if node.right:
                queue.append(node.right)  # Add the right child to the queue

        # Return Result List
        return result
    
# Testing
solution = Solution()


# Expects 3
node1 = TreeNode(15)
node2 = TreeNode(7)
node3 = TreeNode(20, node1, node2)
node4 = TreeNode(9)
tree1 = TreeNode(3, node4, node3)
print("Tree 1:                    ", solution.printLevelOrder(tree1))
print("(Recursive DFS) Max Depth: ", solution.maxDepth(tree1))
print("BFS Max Depth:             ", solution.maxDepth2(tree1), "\n")


# Expects 2
node1 = TreeNode(2)
tree2 = TreeNode(1, None, node1)
print("Tree 2:                    ", solution.printLevelOrder(tree2))
print("(Recursive DFS) Max Depth: ", solution.maxDepth(tree2))
print("BFS Max Depth:             ", solution.maxDepth2(tree2))

"""
R-eview: 
    - Both of the solutions are from NeetCode, I'm not too familiar with trees
      but I do have a basic understanding of DFS and BFS.
    - Need to review in-order, pre-order, and post-order again.
    - Looking at the solutions I understand how the algorithm works in Python
      and can use it in further problems I may come across

E-valuate:
    - For both algorithms, the implementations Space Time Complexity are both
    O(n). Since we are traversing every node in the tree to evaluate the depth
    of the tree. For the BFS, the space is O(n) because we are storing all the
    nodes into a queue. For the Recursive DFS the space is O(n) because in the
    worst case the tree can be skewed, where all the nodes are going to one side
    which resembles something of a singly linked list. The call stacks will have
    n function calls for every node.

"""