# LC 973: K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
# Yzer De Gula

from typing import List
import math
import heapq

"""
U-nderstand:
    # ? What is our input ?
        Our input is an array of points where points[i] = [xi, yi] represents a
    point on the X-Y plane and an integer k.
    # ? What is our output ?
        Our output is the k closest points to the origin (0,0).
    # ? How do we calculate the distance between two points ?
        The distance between two points on the X-Y plane is the Euclidean
    distance is sqrt((x1 - x2)^2 + (y1 - y2)^2).
    # ? Does the order of which we return the points matter ?
        The problem states that we can return the answer in any order.
    # ? Are the points distinct ?
        The problem states that the answer is guranteed to be unique.
    # ? Can the input points be empty ?
        The constraints that the minimum number of elements in our input array
    is 1.
    # ? Can k be greater than the length of the input array ?
        The constraints state that k is ensured to be always less than or equal
    to the length of the input array.

M-atch:
        For this problem, I'm thinking we can use a Heap, and in Python the default
    is a min heap. This isn't a problem since this is what we want. I think we can
    declare a list where we would iterate over the input array and calculate and
    append the distance to the list. We can then heapify that list. We can then
    have a result list where we pop k times from the pop and return that. 

P-lan:
    1) Declare our result and heap lists
    2) Iterating over the input array
        i) Calculate the distance of the point from the origin (0,0)
        ii) Append that value to the list
    3) We can then heapify the list 
    4) Iterating k times
        i) Pop from heap and append it to the result list
    5) Return the result

I-mplement:
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Create our lists
        heap, result = [], []

        # Iterating over the input array
        for x, y in points:
            # Calculate and append the distance using the formula
            distance = math.sqrt(pow(0 - x, 2) + pow(0 - y, 2))
            heap.append([distance, x, y])
        
        # Heapify the list
        heapq.heapify(heap)

        # Iterating k times
        for i in range(k):
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        # Return result
        return result


    def display(self, points: List[List[int]], k: int) -> None:
        print(f"Input: points = {points}, k = {k}")
        print(f"Output: {self.kClosest(points, k)}\n")


# Testing
test = Solution()


# Expects [[-2, 2]]
points, k = [[1,3], [-2,2]], 1
test.display(points, k)

# Expects [[3,3], [-2,4]]
points, k = [[3,3], [5,-1], [-2,4]], 2
test.display(points, k)