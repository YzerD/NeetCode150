# LC 21: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Yzer De Gula

from typing import Optional
from typing import List

"""
U-nderstand:
    - What is our input?
        Out input is two ListNodes that represent the heads of two sorted
        linked lists.
    - What is our output?
        Our output is the head of the merged linked list
    - Can either or both of the linked lists be empty?
        Yes, in the constraints the problem states that the number of nodes in
        both lists is in the range [0,50]
    - Can we have negative values in the nodes?
        Yes, the constraints state that the values of a node can range from -100
        to 100
    - Are the lists sorted?
        Yes, both lists are sorted in non-decreasing order (ascending)
    
    Happy Case:
    Input: list1 = [1,2,3,4], list2 = [2,3,5]
    Output: [1,2,2,3,3,5]

    Input: list1 = [5], list2 = [7,8]
    Output: [5,7,8]

    Edge Case:
    Input: list1 = [], list2 = []
    Output: []

M-atch:
    For Linked List problems, common pattern for solutions include:
        1) Multiple Pass
        2) Temp Head
        3) Two Pointer
    
    Multiple pass wouldn't be needed because we only need to go through both
    linked lists once. Temp Head can be useful so that we can handle the edge
    cases. Two Pointer wouldn't be neccessary since we don't need to iterate
    through the lists at different positions or speeds.

    So I think we would first create our temp node. Then we would have another
    node that tracks the current node we're at. We would then have a while loop
    that goes while both lists have a node present. We would then make the 
    comparison of the node's value. Once we have exhausted one (or both) of the
    lists we would set the current node's next to either list. Finally, we 
    would then return temp.next

P-lan:
    1) Declare Temp Node
    2) Declare Current and set it to temp
    3) While there is a node in both lists
    4) If the node in the first list is less than the second
    5) Set it to current.next
    6) Otherwise, the second node is less than the first
    7) Set it to current.next
    8) After we've exhausted one or both the lists set current.next to either list
    9) Return temp.next

I-mplement:
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Declare Temp Node
    temp = ListNode()

    # Declare Current Pointer
    current = temp

    # While there is a node in both lists
    while list1 and list2:
        # If the first is less than the second
        if list1.val <= list2.val:
            # Set it to the current's next and traverse further
            current.next = list1
            list1 = list1.next

        # Otherwise, second is less than first
        else:
            # Set it to current.next and traverse further
            current.next = list2
            list2 = list2.next
        # Update current pointer
        current = current.next
    
    # Once we've exhausted one or both the list, append any remaining elements
    current.next = list1 or list2

    # Return the temp.next
    return temp.next


list1 = ListNode(5)
node1 = ListNode(8)
list2 = ListNode(7,node1)

print("List 1: ")
node = list1
while node:
    print(node.val)
    node = node.next

print("List 2: ")
node = list2
while node:
    print(node.val)
    node = node.next

print("Merged List: ")
list3 = mergeTwoLists(list1, list2)
node = list3
while node:
    print(node.val)
    node = node.next


print("\n")


node2 = ListNode(4)
node3 = ListNode(2,node2)
list4 = ListNode(1,node3)

print("List 1: ")
node = list4
while node:
    print(node.val)
    node = node.next

node4 = ListNode(4)
node5 = ListNode(3,node4)
list5 = ListNode(1,node5)

print("List 2: ")
node = list5
while node:
    print(node.val)
    node = node.next

# Expects [1,1,2,3,4,4]
print("Merged List: ")
list6 = mergeTwoLists(list4, list5)
node = list6
while node:
    print(node.val)
    node = node.next