# LC 981: Time Based Key-Value Store
# Link: https://leetcode.com/problems/time-based-key-value-store/
# Yzer De Gula

"""
U-nderstand:
    # ? What is our input ?
        Since we're making a class, our input will be the class itself.
    We'll be using a dictionary to store our key, value, and timestamp.
    We will be using the set() and get() methods to manipulate the class.
    set() will take in a key, value, and timestamp. get() will take in a 
    key and timestamp.
    # ? What is our output ?
        set() will return None. get() will return the value of the key
    at the timestamp or an empty string if the key does not exist.
    
M-atch:
        For our constructor we will initialize our dictionary. For set() we will
    add the key, value, and timestamp to our dictionary. The key will be the
    key itself and the value will be a tuple of the value and timestamp. For
    get() we declare our result variable to be an empty string. Since the 
    problem states that if there are no values, to return "". We will then 
    declare our left and right pointers for our binary search. While our
    left and pointers haven't crossed, we can calculate the middle index
    and check if the middle index is less than or equal to our timestamp.
    If so, we can update our left pointer to middle + 1 and update our result
    to the value of the middle index. If not, we can update our right pointer
    to middle - 1. Once our pointers have crossed, we can return our result.
    For set() we can first check if the key is not in the map. If so, we can
    add the key to the map and set the value to be a list of tuples with the
    first element being the value and the second element being the timestamp.
    If the key is in the map, we can append the tuple to the list. 

P-lan:
    Constructor:
        1) Initialize dictionary

    set():
        1) Check if key is not in dictionary
            a) Add key to dictionary
        2) Otherwise, we know the key is in the dictionary
            a) Append tuple to list

    get():
        1) Declare result variable to be empty string
        2) Declare left and right pointers
        3) While left and right pointers haven't crossed
            a) Calculate middle index
            b) Check if middle index is less than or equal to timestamp
                i) Update left pointer to middle + 1
                ii) Update result to value of middle index
            c) Otherwise, update right pointer to middle - 1
        4) Return result

I-mplement:
"""

class TimeMap:
    def __init__(self):
        # Declare dictionary
        self.map = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        # Check if key is not in dictionary
        if key not in self.map:
            # Add the key to the dictionary
            self.map[key] = [(value, timestamp)]
        # Otherwise, we know the key is in the dictionary
        else:
            # Append the tuple to the list
            self.map[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        # Declare result variable to be empty string
        result = ""

        values = self.map.get(key, [])

        # Declare left and right pointers
        left, right = 0, len(values) - 1

        # While left and right pointers haven't crossed
        while left <= right:
            # Calculate middle index
            middle = (left + right) // 2

            # Check if middle index is less than or equal to timestamp
            if self.map[key][middle][1] <= timestamp:
                # Update left pointer to middle + 1
                left = middle + 1

                # Update result to value of middle index
                result = self.map[key][middle][0]

            # Otherwise, update right pointer to middle - 1
            else:
                right = middle - 1
            
        # Return result
        return result


# Testing
test = TimeMap()
test.set("foo", "bar", 1)
print(test.get("foo", 1))
print(test.get("foo", 3))
test.set("foo", "bar2", 4)
print(test.get("foo", 4))
print(test.get("foo", 5))


"""
R-eview:
        I ran into an error with the get() function, it was giving me a key error.
    I had values = self.map[key] which was giving me the error. What this did
    was it would try to access the key in the dictionary and if it didn't exist
    it would throw a key error. 
        To fix this, I looked at NeetCode's solution and saw that they used
    values = self.map.get(key, []) which would return an empty list if the key
    didn't exist. This would allow me to access the list and not throw an error.

E-valuate:
        The time complexity for set() is O(1) since we are just adding to the
    dictionary. The time complexity for get() is O(log n) since we are using
    binary search to find the value. The space complexity is O(n) since we are
    using a dictionary to store our key, value, and timestamp.
    
"""