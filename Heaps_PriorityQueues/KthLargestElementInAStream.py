# LC 703: Kth Largest Element in a Stream
# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Yzer De Gula

from typing import List
import heapq

"""
U-nderstand:
    # ? What is our input ?
        For our constructor, our input is an integer k, and an array of
    integers, nums.
    # ? What is our output ?
        Besides our constructor, our class has one other function named add,
    this function appends the integer, val, to the stream and returns the
    element representing the kth largest element in the stream.
    # ? What is the kth largest element in a stream ?
        The kth largest largest element in sorted order, not the kth distinct
    element.
    # ? Can k or the input array be 0 ?
        No, the the minimum number k can be is 1 and the minimum length of our
    input array is 0.
    # ? Is it guranteed for k elements to exist in the array when we search ?
        Yes, it is guranteed that there will be at least k elements in the
    array when searching for the kth element.

M-atch:
        For this problem we can implement our class using a Min Heap of size k.
    The reason for this being that with the structure of a Min Heap, the top
    of the heap would be the kth largest element in the stream. So in Python we
    can use the heapq library and by default the heap is implemented as a min 
    one. 
        For the constructor we can declare the member variables and then
    heapfiy the nums array. The other caveat would be creating our min heap of
    size k. To do this we can have a while loop that checks while the length of
    the heap is greater than k we pop from the heap.
        For the add function, we can push the value onto the heap and pop any
    values to ensure the min heap of size k property is intact. We can then
    return the top of the heap to get the largest element in size k.

P-lan:
    For constructor:
        1) Declare our data member variables
        2) Heapify our nums array
        3) While the length of the heap is greater than k
            i) Pop from the heap
    
    For add:
        1) Push the element onto the heap
        2) If the length of the heap is greater than k
            i) pop from the heap
        3) Return the top of the heap

I-mplement:
"""

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Declare our data member variables
        self.minHeap, self.k = nums, k

        # Heapify our nums array
        heapq.heapify(nums)

        # While the length of the heap is greater than k
        while len(self.minHeap) > k:
            # Pop the heap
            heapq.heappop(self.minHeap)

    
    def add(self, val: int) -> int:
        # Push the value onto the heap
        heapq.heappush(self.minHeap, val)

        # If the length of the heap is greater than k
        if len(self.minHeap) > self.k:
            # Pop the heap
            heapq.heappop(self.minHeap)

        # Return the top of the heap
        return self.minHeap[0]


# Testing 
test = KthLargest(3, [4, 5, 8, 2])
print(test.add(3))      # Expects 4
print(test.add(5))      # Expects 5
print(test.add(10))     # Expects 5
print(test.add(9))      # Expects 8
print(test.add(4))      # Expects 8