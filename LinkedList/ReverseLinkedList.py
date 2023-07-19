# LC 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Yzer De Gula

from typing import Optional, List

"""
U-nderstand:
    - What is our input?
        Our input is the head of a singly linked list
    - What is our output?
        Our output is the head of the reversed list
    - Can the list be empty?
        Yes, the number of nodes in the list can range from 0 to 5000

M-atch:
    For Linked List problems, common patterns for solutions include:
        1) Multiple Pass
        2) Two Pointer
        3) Temp Head

    Multiple passes would not help solve the problem since we only want
    to traverse the list once. Temp Head wouldn't help because we know
    our starting point. Two Pointer is the viable option since we want
    to keep track of the previous node and the current one so we can do
    a swap.

P-lan:
    1) Declare our two pointers, prev and curr
    2) While there is still something in our Linked List
    3) Store what curr is pointing to in a variable
    4) Set curr.next to prev
    5) Set prev to current 
    6) Set current to the stored next var
    7) Return prev


I-mplement:
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Declare our two pointers
        prev, curr = None, head

        # While there is still something in our list
        while curr:
            # Store what current is currently pointing to
            next = curr.next

            # Set the current node to point to the previous node
            curr.next = prev

            # Set the previous node to the current node to traverse
            prev = curr

            # Set curr to what it originally pointed to
            curr = next
        
        # Return prev
        return prev
    

    def printList(self, head: Optional[ListNode]) -> List[int]:
        # If the list doesn't exist
        if not head:
            # Return an empty list
            return []
        
        # Declare our result list
        result = []

        # While there is still something in our list
        while head:
            # Append the value to our result list
            result.append(head.val)
            # Traverse the list
            head = head.next
        
        # Return the result list
        return result


# Testing
solution = Solution()

# Expects [5,4,3,2,1]
node1 = ListNode(5)
node2 = ListNode(4, node1)
node3 = ListNode(3, node2)
node4 = ListNode(2, node3)
list1 = ListNode(1,node4)

print("Original List: ", solution.printList(list1))
list2 = solution.reverseList(list1)
print("Reversed List: ", solution.printList(list2), "\n")


# Expects [2,1]
node1 = ListNode(2)
list3 = ListNode(1, node1)
print("Original List: ", solution.printList(list3))
list4 = solution.reverseList(list3)
print("Reversed List: ", solution.printList(list4), "\n")


# Expects []
list5 = None
print("Original List: ", solution.printList(list5))
list6 = solution.reverseList(list5)
print("Reversed List: ", solution.printList(list6), "\n")