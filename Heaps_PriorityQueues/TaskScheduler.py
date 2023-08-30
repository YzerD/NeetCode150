# LC 621: Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# Resources Used: https://www.geeksforgeeks.org/python-counter-objects-elements/#
# Yzer De Gula

from typing import List
from collections import deque, Counter
import heapq

"""
U-nderstand:
    # ? What is our input ?
        Our input is a characters array named tasks and an integer named n.
    # ? What is our output ?
        Our output is an integer representing the least amount of time needed
    to finish all the given tasks.
    # ? What does n represent ?
        n represents the cooldown period between two same tasks.
    # ? What is the cooldown period ?
        The cooldown period is the time needed to wait before executing the
    same task again.
    # ? Can our tasks be executed in any order ?
        Yes, our tasks can be executed in any order.
    # ? Can our input array be empty ?
        No, our input array cannot be empty.
    # ? Can n be negative ?
        No, n cannot be negative, it ranges from 0 to 100.
    # ? Can n be greater than the length of our input array ?
        Yes, n can be greater than the length of our input array.
    # ? Can our input array have anything other than uppercase letters ?
        No, our input array can only have uppercase letters.

M-atch:
        For this problem, we can utilize a Max Heap to keep track of the most
    frequent tasks. We can also use a dictionary to keep track of the number
    of times a task has been executed. We can do this simply with the Counter
    class from the collections module. We can also use a variable to keep
    track of the time needed to finish all the tasks. Additionally, we can
    use a double ended queue to keep track of the tasks that are ready to be
    executed. We can use a variable to keep track of the cooldown period.
    While there is still something in our max heap or q, we increment our
    time variable. Then if in the max heap there's a non-zero value, we pop
    it and increment it by 1. If the task count is not zero, we append it
    to the queue as a tuple of the task count and the time plus the cooldown
    period. If our queue is nonempty and the first value of our queue at 
    index 0 is equal to the current time, we pop it and push it to the max
    heap. We return the time variable.

P-lan:
    1) Create a Hash Map of our tasks list using Counter()
    2) Using List Comprehension get the negative values of the Hash Maps values
    3) Heapify that list
    4) Declare our time variable and deque()
    5) While there is something in our Max Heap or queue
        i) Increment our time counter
        ii) Check if there is a non-zero value in our Max Heap
            a) If so, set the task count to 1 plus the popped value from the Max Heap
            b) If the task count is non-zero
                I) Append the tuple of the task count and the time counter plus the
                   cooldown time to the queue
        iii) If the queue is non-empty and the first value of our queue at index 0
             is equal to the current time
             a) We push onto the Max Heap the front of the queue
    6) Return time


I-mplement:
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create our Hash Map using Counter
        task_count = Counter(tasks)

        # Using List Comprehension negate the Hash Maps values
        max_heap = [-count for count in task_count.values()]
        #print(max_heap)

        # Heapify the list
        heapq.heapify(max_heap)

        # Declare our variables
        time = 0
        queue = deque()

        # While there is something in our Max Heap or queue
        while max_heap or queue:
            # Increment time 
            time += 1
            # If there is a non-zero value in our Max Heap
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                # If the count is non-zero
                if count:
                    # Append the tuple [count, time + n] to the queue
                    queue.append([count, time + n])
            # If there is something in our queue and the first value at index 0 is equal to time
            if queue and queue[0][1] == time:
                # This means that the calculated cooldown time for this task is ready
                # So we pop the queue and add it back to the Max Heap
                heapq.heappush(max_heap, queue.popleft()[0])
            
        # Return time
        return time


    def display(self, tasks: List[str], n: int) -> int:
        print(f"Input: tasks = {tasks}, n = {n}")
        print(f"Output: {self.leastInterval(tasks, n)}\n")


# Testing
test = Solution()

# Expected: 8
tasks, n = ["A","A","A","B","B","B"], 2
test.display(tasks, n)

# Expects 6
tasks, n = ["A","A","A","B","B","B"], 0
test.display(tasks, n)

# Expects 16
tasks, n = ["A","A","A","A","A","A","B","C","D","E","F","G"], 2
test.display(tasks, n)