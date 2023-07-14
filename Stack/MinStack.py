# LC 155: Min Stack
# https://leetcode.com/problems/min-stack/
# Yzer De Gula

"""
U-nderstand:
    - What are our class's functions?
        We need to implement a constructor, push, pop, top, getMin
    - What does the constructor do?
        The constructor initializes the stack object
    - What does push do?
        Push pushes the element onto the stack
    - What does pop do?
        Pop removes the top element of the stack
    - What does top do?
        Top gets the top element of the stack
    - What does getMin do?
        GetMin retrieves the minimum element in the stack
    - Does runtime matter?
        Problem states that all function should have a O(1) runtime

M-atch:
    For this we can implement our MinStack class using two stacks. One stack
    for the typical stack operations, and another one to keep track of the 
    minimum element. We can Pushing, we can compare the element we want to
    insert to what's on the min stack (if there is anything on the min stack).
    The reason for this because the runtime to retrieve from the min stack is
    O(1).

P-lan:
    1) Constructor create an empty list
    2) Push, append element to regular stack
    3) For the min stack we compare the element with whatever is on the min
       stack if there is anything
    4) Append the smallest element into the min stack
    5) Pop, pop from both stacks
    6) Top, return top element of stack
    7) getMin, return top element of min stack


I-mplement:
"""

class MinStack:
    # Constructor 
    def __init__(self):
        # Declare our stacks
        self.stack = []
        self.min_stack = []

    # Pushes the element val onto the stack
    def push(self, val: int) -> None:
        # Push val on the stack
        self.stack.append(val)

        # If there is something in our min stack
        if self.min_stack:
            # Take the minimum of the val and what's on top of the min stack
            val = min(val, self.min_stack[-1])
        # Push the min onto the min stack
        self.min_stack.append(val)

    # Pop removes the element on top of the stack
    def pop(self) -> None:
        # Pop both stacks
        self.stack.pop()
        self.min_stack.pop()

    # Top gets the top element of the stack
    def top(self) -> int:
        # Return top of stack
        return self.stack[-1]
    
    # getMin retrieves the minimum element in the stack
    def getMin(self) -> int:
        # Return top of min stack
        return self.min_stack[-1]
    

minstack1 = MinStack()
minstack1.push(-2)
minstack1.push(0)
minstack1.push(-3)
print("Stack:   ", minstack1.stack)
print("Minimum: ", minstack1.getMin())
print("Top:     ", minstack1.top())

minstack1.pop()
print("After Popping: ")
print("Stack:   ", minstack1.stack)
print("Minimum: ", minstack1.getMin())
print("Top:     ", minstack1.top())