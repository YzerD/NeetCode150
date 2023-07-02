from typing import List

# LC 217: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Yzer De Gula

def containsDuplicate(nums: List[int]) -> bool:
    # Declare our Hash Set
    nums_set = set()

    # Iterating over the array
    for i in nums:
        # If the number we're trying to put it in,
        # is already present in the set
        if i in nums_set:
            # Return True
            return True
        # Otherwise,
        else:
            # Add it to the set
            nums_set.add(i)

    # After iterating, if not dupes found, return false 
    return False

nums_1 = [1,2,3,1] 
# Expects True
print(containsDuplicate(nums_1))

nums_2 = [1,2,3,4]
# Expects False
print(containsDuplicate(nums_2))

nums_3 = [1,1,1,3,3,4,3,2,4,2,]
# Expects True
print(containsDuplicate(nums_3))

