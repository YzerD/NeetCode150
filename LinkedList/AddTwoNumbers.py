# LC 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Yzer De Gula

from typing import Optional, List

"""
U-nderstand:
    # ? What is our input ?
        Our input is two NON-EMPTY linked lists representing two NON-NEGATIVE
    integers.
    # ? What is our output ?
        Our output is the sum returned as a linked list
    # ? Is there any restrictions on runtime or memory?
        From my knowledge, there is no specifications regarding runtime or 
    memory for this problem listed.
    # ? How are the numbers stored ?
        The numbers are stored in reverse order, and each of their nodes
    contain a single digit.
    # ? Are there any leading zeros ?
        The problem states that we can assum that the two numbers do not 
    contain any leading zeroes, excpet the number 0 itself.


M-atch:
    For Linked List problems, common patterns for solutions include:
        1) Multiple Pass
        2) Two Pointers
        3) Temp Head
    
        For this problem, Two Pointers wouldn't help reach a solution. Temp Head
    will also not be useful since we know our starting point. This leaves 
    Multiple Pass, which can be useful since we would need to calculate the sum
    first and then constrcut the linked list. I think what we can do first is to
    declare variables to store the numbers from list 1 and 2. Since we know that
    it's in reverse order we can append the value of that node multiplied by 10
    raised to the power of that node's position. Take 243 in example 1, the
    number that it's supposed to represent is 342. So in our num1 variable we 
    can have 2 * 10^0 = 2, 4 * 10^1, 3 * 10^2. Where 2 + 40 + 300 = 342. We can
    then add the sum of this and list 2 then use List Comprehension to convert
    the number to string so we can iterate over it and then convert it back into
    an int and then construct our Linked List.


P-lan:
    1) Declare our num1 and num2 variables
    2) Declare a curr pointer to keep track of our traversal
    3) While there's still something in list1
    4) Add the sum of the node's value multipled by 10 to the power of the index
    5) Do the same for list 2
    6) Add num1 and num2
    7) Use List Comprehension to convert the number into a string and then iterate
       over it converting each digit back to an int
    8) Construct the new linked list
    9) Return the head of the new linked list


I-mplement:
"""

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def add(self, value: int) -> None:
        curr = self
        while curr.next:
            curr = curr.next
        node = ListNode(value)
        curr.next = node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Declare our variables
        num1, num2 = 0, 0 

        # Get the number in List 1
        curr = l1
        exp = 0
        while curr:
            num1 += curr.val * pow(10, exp)
            exp += 1
            #print(f"Num1: {num1}")
            curr = curr.next


        # Get the number in List 2
        curr = l2
        exp = 0
        while curr:
            num2 += curr.val * pow(10, exp)
            #print(f"Num2: {num2}")
            exp += 1
            curr = curr.next

        # Get the sum of num1 and num2
        sum = num1 + num2
        #print(f"Sum: {sum}")

        # Seperate the digits in the sum
        sum_list = [int(n) for n in str(sum)]
        sum_list.reverse()
        #print(f"Sum List = {sum_list}")

        # Construct the new list
        temp = ListNode()
        curr = temp
        for i in sum_list:
            curr.next = ListNode(i)
            curr = curr.next
        
        # Return the head of the new Linked List
        return temp.next
    
    
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
    

    def display(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        print(f"Input: l1 = {self.printList(l1)}, l2 = {self.printList(l2)}")
        print(f"Output: {self.printList(self.addTwoNumbers(l1, l2))}\n")


# Testing 
test = Solution()

# Expects [7,0,8]
list1 = ListNode(2)
list1.add(4)
list1.add(3)

list2 = ListNode(5)
list2.add(6)
list2.add(4)

test.display(list1, list2)


# Expects [0]
list1 = ListNode(0)
list2 = ListNode(0)
test.display(list1, list2)


# Expects [8,9,9,9,0,0,0,1]
list1 = ListNode(9)
list1.add(9)
list1.add(9)
list1.add(9)
list1.add(9)
list1.add(9)
list1.add(9)


list2 = ListNode(9)
list2.add(9)
list2.add(9)
list2.add(9)

test.display(list1, list2)