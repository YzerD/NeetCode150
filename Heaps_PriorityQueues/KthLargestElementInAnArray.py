# LC 215: Kth Largest Element in an Array (Medium)
# https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
Question:
  Given an integer array nums and an integer k, return the kth largest element in the array.
  Note that it is the kth largest element in the sorted order, not the kth distinct element.
  Can you solve it without sorting?


Example 1:
  Input: nums = [3,2,1,5,6,4], k = 2
  Output: 5

Example 2:
  Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
  Output: 4

 
Constraints:
  1 <= k <= nums.length <= 105
  -104 <= nums[i] <= 104

UNDERSTAND:
1. Will k ever be greater than size of nums? No
2. Space and time constraints? O(n) and O(n)
  aka extra space is allowed and it needs to run in linear time
3. k will always be less than or equal to the array. 

Edge cases:
1. Empty nums array with k = 0
  --> this won't happen
2. Single element in nums array with k = 1
  --> return that element 

  
  1 <= k <= nums.length <= 105
  

MATCH:
- We are dealing with an UNSORTED array and we want to find not the largest element, 
but the kth largest element..

- If we sort the array, this will result in O(nlogn) to sort 
  --> Therefore, it violates the O(n) runtime requirement

- We know we have to process every single element in the array 
  AND we know we can only iterate through the array ONCE 
  in order to maintain a O(n) runtime

- BUT we also know we can use O(n) extra space, 
  THEREFORE, we can iterate through the array once and store our elements somewhere...

- WHERE?? What data structure helps us keep track of elements in a "sorted" way?
  HEAPS/PRIORITY QUEUES!! 

- We need a heap/priority queue that holds the k largest elements
  A max heap sounds appropriate, but the max number will be at the top
    and we don't want to get rid of the max number, we want to get rid of any number that
    is trying to be inputted but the size is already k (although we CAN remove k from maxHeap)
  A min heap will hold the min number at the top, and we can restrict the size of our heap
    to only hold k elements, making less calls to the heap/size. This way, 
    we can return the top being the kth largest element. 

TL;DR  - Use a min heap data structure 

PLAN:
1. Create a min heap/priority queue 
2. Loop through the nums array adding the the heap
3.   If the size of heap > k, remove elements from the heap 
4. Return top of the heap
"""

import heapq


def kthLargest(nums, k):
  # Create a new list so that we can create a heap
  heap = [-num for num in nums]

  #for num in nums:
  #heap.append(-num)

  # Create our max heap
  heapq.heapify(heap)

  # For k times
  for i in range(1, k):
    # Pop heap
    heapq.heappop(heap)

  # Return Top of heap
  return -heap[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
#output should be 5
print("Kth largest element is: " + str(kthLargest(nums, k)))

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
#output should be 4
print("Kth largest element is: " + str(kthLargest(nums, k)))
