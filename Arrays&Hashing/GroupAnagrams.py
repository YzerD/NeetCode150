# LC 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Yzer De Gula

from typing import List

"""
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original
letters exactly once.


Example 1:
    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
    Input: strs = [""]
    Output: [[""]]

Example 3:
    Input: strs = ["a"]
    Output: [["a"]]


Constraints:
    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.
"""


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # Get length of strings array
    length = len(strs)

    # Sort and store the strings in a new array
    strs_sorted = []
    for i in strs:
        strs_sorted.append(''.join(sorted(i)))

    # Store the sorted array in a Hash Map
    strs_map = dict()

    # Have the key as the string and the value as the index
    for i in range(length):
        # If the sorted string is already in the map,
        if strs_sorted[i] in strs_map:
            # Append it to the already existing key
            strs_map[strs_sorted[i]].append(strs[i])
        # Otherwise, the key isn't present
        else:
            # Therefore we add it to the map
            strs_map[strs_sorted[i]] = [strs[i]]

    # Take the values from the Hash Map to create a List of Lists
    strs_result = []
    for value in strs_map.values():
        strs_result.append(value)

    return strs_result


# Expects [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
strs_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs_1))

# Expects [[""]]
strs_2 = [""]
print(groupAnagrams(strs_2))


# Expects [["a"]]
strs_3 = ["a"]
print(groupAnagrams(strs_3))