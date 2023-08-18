# LC 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Yzer De Gula

from typing import Optional

"""
U-nderstand:
    # ? What is the input ?
        Our input is the head of a linked list
    # ? What is the output ?
        Our output is a boolean value indicating whether or not the linked list has a cycle
    # ? What are the constraints ?
        0 <= Node.val <= 10^5
        The number of nodes in the list is in the range [0, 10^4]
        -10^5 <= Node.val <= 10^5
    # ? What are some edge cases ?
        If the head is None, return False
    
M-atch:
    For Linked List problems, common patterns for solutions are:
        1) Hash Table
        2) Two Pointers
        3) Multiple Pass

    
    For this problem, we can use the Two Pointer pattern to solve it.
    We can have two pointers, one that moves one node at a time and another that moves two nodes at a time.
    If the two pointers ever meet, then we know that there is a cycle in the linked list.
    If the fast pointer ever reaches the end of the list, then we know that there is no cycle in the linked list.

P-lan:
    1) Declare our two pointers, slow and fast
    2) While fast is not None and fast.next is not None
    3) Set slow to slow.next
    4) Set fast to fast.next.next
    5) If slow is equal to fast, return True
    6) Return False

I-mplement:
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Declare our two pointers
        slow, fast = head, head

        # While fast is not None and fast.next is not None
        while fast and fast.next:
            # Set slow to slow.next
            slow = slow.next

            # Set fast to fast.next.next
            fast = fast.next.next

            # If slow is equal to fast, return True
            if slow == fast:
                return True
        
        # Return False
        return False


# Testing
# Expects True
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)

head.next.next.next.next = head.next
print(Solution().hasCycle(head))

# Expects True
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(Solution().hasCycle(head))

# Expects False
head = ListNode(1)
print(Solution().hasCycle(head))
