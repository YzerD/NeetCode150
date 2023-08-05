# LC 997: Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/
# Yzer De Gula

from typing import List

"""
U-nderstand:
    # ? What is our input ? 
        Our input is n, representing the number of people in a town, labeled
        from 1 to n. There is also an array labeled trust, where it's a tuple
        of two people, the first index representing a person, and the second
        represent who they trust.
    # ? What is our output?
        Our output is the label of the town judge
    # ? What are the properties of a town judge ?
        If the town judge exists, then:
            1.) The town judge trust nobody
            2.) Everybody (except the town judge) trusts the town judge
            3.) There is exactly one person that satisfies properties 1 and 2
    # ? Is there guranteed for a town judge to exist ?
        No, in the case the town judge can't be identified we return -1
    # ? Can someone trust themselves ?
        No, the constraints of the problem state that ai != bi, meaning that
        a person cannot trust themselves. 

M-atch:
    This town can be represented as a graph, with the trust list acting as
    a adjacency list. Where each element in the list represents an edge.
    We can create a list of size n + 1, since the people are labeled using
    1 - indexing. Given the properties of what constitutes as a town judge
    we want to calculate the net trust count of the townspeople and see
    whose trust count is equal to n - 1. The reason it's n - 1 is that the
    judge cannot trust themselves, but must have everyone else trust them.
    So we can iterate through the trust list, seperating ai and bi, we
    decrement ai since people are unable to trust themselves and therefore
    has to trust someone else, and increment bi. After that, we can iterate
    through the trust count list, and see if any trust count is equal to n - 1.
    If so, return that label. If we're unable to identify the town judge,
    return -1. 

P-lan:
    1) Create a list of size n + 1 for 1 - indexing
    2) Iterate through the trust list, seperating person 1 and person 2
    3) Decrement person1
    4) Increment person2
    5) Iterate over the trust count list (1 - indexing)
    6) If any trust count is equal to n - 1, return that index
    7) Otherwise, return -1


I-mplement:
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create a list of size n + 1
        count = [0] * (n + 1)

        # Iterating over the trust list, seperating the tuple
        for person1, person2 in trust:
            # Decrement person1
            count[person1] -= 1
            # Increment person2
            count[person2] += 1

        # Iterating over the trust count list (1 - indexed)
        for i in range(1, len(count)):
            # If any net trust count equal to n - 1
            if count[i] == n - 1:
                # Return that index
                return i
        
        # If the town judge doesn't exist, return -1 
        return -1

    
    def display(self, n: int, trust: List[List[int]]) -> None:
        print(f"Input: n = {n}, trust = {trust}")
        print(f"Output: {self.findJudge(n, trust)}\n")
    

# Testing 
sol = Solution()

# Expects 2
n = 2
trust = [[1,2]]
sol.display(n, trust)

# Expects 3
n = 3
trust = [[1,3], [2,3]]
sol.display(n, trust)

# Expects -1
n = 3
trust = [[1,3], [2,3], [3,1]]
sol.display(n, trust)