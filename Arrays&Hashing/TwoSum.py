from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Get the length of the array
    length = len(nums)

    # Iterating over up to the last element in the array,
    for i in range(length - 1):
        # Iterating every index beyond the first one up to the end of the array
        for j in range(i + 1, length):
            # If their sum equals the target
            if nums[i] + nums[j] == target:
                # Return their indicies
                return [i, j]


def twoSumHash(nums: List[int], target: int) -> List[int]:
    # Create our Hash Map
    nums_map = dict()

    # Iterating over the length of the array
    for i in range(len(nums)):
        # Store the value as the key and its index as the value
        nums_map[nums[i]] = i 

    # Itearting over the Hash Map
    for i in range(len(nums)):
        # Calculate the complement
        complement = target - nums[i]
        
        # If the complement is in the map and it's a distinct index
        if (complement in nums_map) and (nums_map[complement] != i):
            # Return their indicies
            return [i, nums_map[complement]]


# Expects [0,1]
nums_1 = [2,7,11,15]
print("Two Sum (For Loop): ", twoSum(nums_1, 9))
print("Two Sum (Hash Map): ", twoSumHash(nums_1, 9))

# Expects [1,2]
nums_2 = [3,2,4]
print("Two Sum (For Loop): ", twoSum(nums_2, 6))
print("Two Sum (Hash Map): ", twoSumHash(nums_2, 6))

# Expects [0,1]
nums_3 = [3,3]
print("Two Sum (For Loop): ", twoSum(nums_3, 6))
print("Two Sum (Hash Map): ", twoSumHash(nums_3, 6))