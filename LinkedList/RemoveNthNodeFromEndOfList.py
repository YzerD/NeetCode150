# LC 19: Remove Nth Node From End Of List (Medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional
"""
Question:
    Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
  Input: head = [1,2,3,4,5], n = 2
  Output: [1,2,3,5]
  
Example 2:
  Input: head = [1], n = 1
  Output: []
  
Example 3:
  Input: head = [1,2], n = 1
  Output: [1]

Constraints:
  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz

U-nderstand:
 - How can we remove the nth node from the end of the linked list if were given the head and nth node of the list. What do we return after performing operation?

M-atch:
 - Traverse Linked List
 - Delete Node in Linked List

P-lan:
Initial Plan:
 - Initialize pointers/nodes
 - Initalize linked list
 - traverse through linked list
 - once nth head is found, remove head
 - return head of new linked list

Big Brain Time:
  1) Initialize Temp node and set it to the head of the lsit
  2) Initialize 2 pointers
      - The first one is starting in the temp node (slow)
      - The second one would be nth nodes away from the first node (fast)
  3) While the next node of the fast ISN'T null
      - Increment both pointers
  4) If the next node of the fast pointer IS null
      - Delete the next node of the slow pointer
  5) Return temp.next
  6) Profit (:

I-mplement:
"""

class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      # Initializing temp node 
      temp = ListNode(val = 0, next = head)

      # Initializing pointers 
      fast, slow = temp, temp

      # incrementing the fast pointer to the nth node
      for i in range(n):
        fast = fast.next

      # if fast:     There
      # if not fast: Isn't
      
      # While fast.next isn't null
      while fast.next is not None:
      # Move both pointer until fast pointer reaches end of list
        fast = fast.next
        slow = slow.next

      # Remove nth node
      slow.next = slow.next.next
      
      # Return head
      return temp.next