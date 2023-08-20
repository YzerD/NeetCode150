# LC 138: Copy List With Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Yzer De Gula

from typing import Optional, List

"""
U-nderstand:
    # ? What is our input ?
        Our input is a linked list of length n, where each node contains an
    additonal random pointer, which could point to any node in the list, or null
    # ? What is our ouput ?
        Our output is the head of the copied linked list
    # ? What kind of copy are we doing ?
        We are doing a deep copy of the list. A deep copy is when we create an
    entirely new copy of that structure. This means that changes made to the 
    original copy won't affect the deep copy, and vice versa.
    # ? How are the nodes represented ?
        The nodes of the linked list are represented as a pair of
    [val, random_index] where val is an integer representing Node.val. 
    random_index the index of the node (range from 0 to n - 1) that the random
    pointer points to, or null if it does not point to any node. 

M-atch:
    For Linked List problems, common patterns for solutions include:
        1) Multiple Pass
        2) Two Pointer
        3) Temp Head

        For this problem, we don't need a temp head since we know what our start
    point is. We don't need to use two pointers since it'll complicate our code.
    We can do multiple pass, two to be more specific. The first pass will create
    all copy nodes and store them in a Hash Map. The reason we're storing them 
    in a Hash Map and multiple pass is because if we were to construct the Linked
    List one node at a time, the random pointer might point to a node that we 
    haven't constructed yet. So if we have all the nodes and their copies in the
    Hash Map, we can easily reference them. So the second pass is linking all 
    the nodes together. We have to set the next and random data members of each
    node. After we can return the head of the linked list from our Hash Map.

P-lan:
    1) Declare our Hash Map
        a) Have the Base Case where None : None
    2) Create a curr var set to the head
    3) While curr isn't null
        a) Create the copy node with the old node's value
        b) Store the old node as the key and the copy node as the value 
        c) Update the curr node to the next one
    4) Reset the curr node to the head of the old list
    5) While curr isn't null
        a) Get the copy node set to the value stored by the Hash Map
        b) Set the next data member to the old node's next value
        c) Set the random data member to the old node's random value
        d) Update the curr node to the next one
    6) Return the Head of the copied Linkd List


I-mplement:
"""

class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        # Create our Hash Map
        oldToCopy = { None : None }

        # Create a curr pointer to keep track of traversal
        curr = head
        # Create the copy node, and store the old node as the key, and copy as value
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next


        # Reset current pointer, and link the Nodes 
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        # Return the head of our copied linked list
        return oldToCopy[head]
        

    def printList(self, head: "Optional[Node]") -> "List[int]":
        # If the list doesn't exist
        if not head:
            # Return an empty list
            return []
        
        # Declare our result list
        result = []

        # While there is still something in our list
        while head:
            # Append the value to our result list
            result.append((head.val, head.random))
            # Traverse the list
            head = head.next
        
        # Return the result list
        return result


# Testing
test = Solution()

# Expects [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head
print("Input:   ", test.printList(head))
print("Output:  ", test.printList(test.copyRandomList(head)))


# Expects [[1,1],[2,1]]
head = Node(1, Node(2))
head.random = head.next
head.next.random = head.next
print("Input:   ", test.printList(head))
print("Output:  ", test.printList(test.copyRandomList(head)))


# Expects [[3,null],[3,0],[3,null]]
head = Node(3, Node(3, Node(3)))
head.next.random = head
print("Input:   ", test.printList(head))
print("Output:  ", test.printList(test.copyRandomList(head)))