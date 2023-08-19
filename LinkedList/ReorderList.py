# LC 143: Reorder List
# https://leetcode.com/problems/reorder-list/
# Yzer De Gula

from typing import Optional, List

"""
U-nderstand:
    # ? What kind of Linked List is it ?
        It is a singly linked list
    # ? What is our input ?
        Our input is the head of a singly linked list
    # ? What is our output ?
        Our output is nothing since we aren't returning anything
    # ? Can the list be empty ?
        No, the number of nodes in the list is in the range [1, 5 * 10^4]
    # ? Can the list have only one node ?
        Yes, and if so we return the list as is
    # ? How do we reorder the list ?
        We can reorder the list by taking the first node and pairing it with
        the last node and so on until we reach the middle of the list


M-atch:
    For Linked List problems, common patterns for solutions include:
        1) Multiple Pass
        2) Two Pointer
        3) Temp Head

        A naive soluition for this problem would be to store all the node's values
    in an array and then use two pointers to traverse the array and reorder the
    list. This would take O(n) space and O(n) time. A better solution would be
    to use two pointers to find the middle of the list and then reverse the second
    half of the list. Then we can use two pointers to merge the two lists together.
    This would take O(1) space and O(n) time.

        But how do we find the middle of a Linked List? We can use a slow and a
    fast pointer. The slow pointer will move one node at a time while the fast
    pointer will move two nodes at a time. When the fast and fast.next pointers
    are None, we know that the slow pointer is at the middle of the list.

        How do reverse the second half of the Linked List? We can use the same
    approach as LC 206: Reverse Linked List. We can use two pointers, prev and
    curr, to reverse the list. We can set prev to None and curr to the head of
    the second half of the list. Then we can traverse the list and set curr.next
    to prev and then set prev to curr and curr to curr.next. We can return prev
    as the head of the reversed list.

        How do we merge the two lists together? We can use two pointers, l1 and
    l2, to traverse the two lists. We can set l1 to the head of the first half
    of the list and l2 to the head of the reversed second half of the list. Then
    we can traverse the list and set l1.next to l2 and then set l1 to l2 and l2
    to l1.next. We can return the head of the list.
    

P-lan:
    Naive Solution:
        1) Check if the list is empty or only has one node
        2) Declare an array
        3) Traverse the list and append the nodes to the array
        4) Declare two pointers, left and right, and set them to 0 and the
           length of the array - 1
        5) While our two pointers haven't crossed
        6) Set the next node of the left node to the right node
        7) Increment left by 1
        8) Set the next node of the right node to the left node
        9) Decrement right by 1
        10) Set the next node of the left node to None
    
        
    Optimal Solution:
        1) Declare two pointers, slow and fast, and set them to the head of the list
        2) While fast and fast.next are not None
        3) Set slow to slow.next and fast to fast.next.next
        4) Declare two pointers, prev and curr, and set them to None and slow
        5) While curr is not None
        6) Store curr.next in a variable (next)
        7) Set curr.next to prev
        8) Set prev to curr
        9) Set curr to next


I-mplement:
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:
    def reorderListNaive(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """ 
        # If the list doesn't exist or only has one node
        if not head or not head.next:
            # Return nothing
            return
        
        # Declare an array
        arr = []

        # Traverse the list
        while head:
            # Append the node to the array
            arr.append(head)
            # Traverse the list
            head = head.next

        # Declare two pointers
        left, right = 0, len(arr) - 1

        # While our two pointers haven't crossed
        while left < right:
            arr[left].next = arr[right]
            left += 1
            arr[right].next = arr[left]
            right -= 1
        
        # Set the next node of the last node to None
        arr[left].next = None

        
    def reorderList(self, head: Optional[ListNode]) -> None:
        # If the list doesn't exist or only has one node
        if not head or not head.next:
            # Return nothing
            return
        
        # Find Middle of List
        slow, fast = head, head.next
        while fast and fast.next:
            # Move slow one node at a time
            slow = slow.next
            # Move fast two nodes at a time
            fast = fast.next.next
        

        # Reverse this second half of the list
        prev, curr = None, slow.next
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Set the next node of the slow pointer to None
        slow.next = None


        # Merge the two lists together
        list1, list2 = head, prev
        while list2:
            # Store list1.next in a variable
            next = list1.next
            # Set list1.next to list2
            list1.next = list2
            # Set list1 to list2
            list1 = list2
            # Set list2 to next
            list2 = next

    
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
test = Solution()

# Expects [1,4,2,3]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
test.reorderListNaive(head)
print("Naive:   ", test.printList(head))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
test.reorderList(head)
print("Optimal: ", test.printList(head))

# Expects [1,5,2,4,3]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test.reorderListNaive(head)
print("Naive:   ", test.printList(head))
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
test.reorderList(head)
print("Optimal: ", test.printList(head))