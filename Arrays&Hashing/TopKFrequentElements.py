# Lc 347: Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Yzer De Gula 

from typing import List

"""
U-nderstand:
    - What is our input?
        Our input is an array of integers, and an integer k
    - What does k represent?
        K represents the amount of most frequent elements we must return
    - What is our output?
        Our output is a list of k size that returns the amount of most frequent
        elements from the input array
    - Can the input array ever be empty?
        No, from the problem's constraints it states that the minimum length of
        the array is 1 and has a max of 10^5.
    - Can k ever be larger than the number of distinct elements in the input
      array?
        No, from the constraints, it states that k is in the range of 1
        (minimum length the input array can be) to the number of distinct
        elements in the array.
    - What if elements have the same number of frequencies?
        The problem states that the answer is guranteed to be unique. 
    
    Happy Case:
    Input: nums = [1,2,3,3,3,4,4,5], k = 2
    Output: [3,4]

    Edge Case:
    Input: nums = [7], k = 1
    Output: [7]

M-atch:
    For Arrays and String problems, common patterns for their solution are:
        1) Sorting
        2) Sliding Window
        3) Two Pointers
        4) Storing in a Hash Map or Set
    
    Considering that we're looking to keep track of frequencies I think the
    best approach is to store the elements in a Hash Map having the key-value
    pair being the value of the integer as the key and its frequency as the
    value. I think we can have a seperate counter to that will be in a while
    loop that will run while it's less than k we'll search the map for the
    highest frequency, append it to a result list and increment the counter.
    We would then return the result list.

P-lan:
    1) Create our Hash Map
    2) Store all the elements from the input array into our Hash Map, value of
       integer as the key and its frequency as the value. 
    3) Declare our counter variable and set it to 0
    4) Create our result list
    5) While the counter is less than k
    6) Get the highest frequency and append it to the list
    7) Remove that key from the Map
    8) Return result

I-mplement:
"""

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Create our Hash Map
    nums_map = dict()

    # Store all the elements from the array into our map
    # Keys are the values of the integer, value is the frequency
    for i in range(len(nums)):
        if nums[i] in nums_map:
            nums_map[nums[i]] += 1
        else:
            nums_map[nums[i]] = 1

    # Declare our counter
    counter = 0

    # Declare our result List
    result = []

    # While our counter is less than k
    while (counter < k):
        # Declare temp variables to keep track of the max
        max_freq = 0
        max_num = 0

        # For the key-value pairs in the map
        for key, value in nums_map.items():
            # If the frequency is greater than the current max
            if (value > max_freq):
                # Update the temp vars
                max_freq = value
                max_num = key
        
        # After finding the max, add it to the list and remove the key
        result.append(max_num)
        nums_map.pop(max_num)

        # Increment our counter
        counter += 1
    
    # Return result list
    return result

"""
R-eview:
    One small oversight I found when trying to find the max frequency in the
map is how I will keep track of it's key value. So that's why there are two
temp vars to store the max's key and frequency. Other than that, the plan
seems to work and passed all the test cases on LC.

E-valuate:
    - I think the Time Complexity is O(n * k) because it takes O(n) time
      to put the elements into the map and the while loop takes k times.
    - I think the Space Compelxity of this is O(n) since we took all the
      elements from the input array and stored it into a Hash Map.
"""


# TEST CASES

# Expects [1,2]
nums_1 = [1,1,1,2,2,3]
print(topKFrequent(nums_1, 2))

# Expects [1]
nums_2 = [1]
print(topKFrequent(nums_2, 1))