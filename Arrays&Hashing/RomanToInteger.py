# LC 128: Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/roman-to-integer/
# Yzer De Gula

"""
# U-nderstand:
    What is our input?
        Our input is a roman numeral, represented ONLY by the characters,
        [I, V, X, L, C, D, and M].
    What is our output?
        Our output is the integer value of the roman numeral.
    When do we subtract the value rather than add it?
        We only subtract if a lesser value is behind a greater value.
        Take I before V and X, or X before L and C. 
    How can we ensure that a lesser value is before a greater value if we're subtracting?
        We don't have to, according to the constraints, the input is a VALID roman
        numeral.
        
# M-atch:
    For arrays and strings, common patterns for solutions include:
        1.) Sorting
        2.) Sliding Window
        3.) Hash Map / Set
        4.) Two Pointers
    
        For this probelm it's clear that a hash map would have to be utilized. Having the
    key value pair for the hash map be the letter and it's value. At the start of our
    function we can declare a variable to keep track of our sum. We can also declare
    our hash map with the roman letter tied to its value. 
        After this, we can start looping through the input string UP UNTIL the very
    last index. This is because we need to check two indicies if the current index 
    is smaller than the next and that could go out of bounds. But in the loop we 
    need to first check if the current index is less than the index one ahead of it.
    If so, we add the difference between the larger and lesser number to the sum and
    go ahead two indicies since we checked those two already. Otherwise, the current
    index isn't smaller than the next and so we just add it to the sum. After we
    looped through this we add the last integer.

# P-lan:
    1.) Create our variable to track our sum.
    2.) Create our hash maps with the letter paired up with its corresponding value.
    3.) Create a current index variable set to 0 to keep track of the index we're at
    4.) While the current index variable is less than the length of the input string - 1
    5.) We check if the current index is smaller than the next one
    6.) If so, we add the difference between the larger and smaller number to the sum.
    7.) Otherwise, we add the value of that letter to the sum.
    8.) After looping, we add the last index's value to the sum.
    9.) Return the sum.

# I-mplement:
"""
def romanToInt(s: str) -> int:
    # Create our sum variable
    sum = 0

    # Create our index variable
    curr_index = 0

    # Get length of string
    length = len(s)

    # Create our Hash Map
    roman_val = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    # Iterating over the string
    for i in range(length - 1):
        # Check if the current index value is less than the larger
        if roman_val[s[i]] < roman_val[s[i + 1]]:
            # Subtract from total
            sum -= roman_val[s[i]]
        # Otherwise, add the value to the sum
        else:
            sum += roman_val[s[i]]
    """
    # While the index is less than the length of the string minus 1
    while curr_index < len(s):
        # Check if the current index is less than the next index
        if curr_index < len(s) - 1 and (roman_val[s[curr_index]] < roman_val[s[curr_index + 1]]):
            # Add the difference of the larger and smaller value to the sum
            sum += roman_val[s[curr_index + 1]] - roman_val[s[curr_index]]
            
            # Update our index variable by 2
            curr_index += 2
        # Otherwise, the current index is NOT smaller than the next
        else:
            # Add its value to the sum
            sum += roman_val[s[curr_index]]

            # Update index variable
            curr_index += 1
    """
    # Return the sum
    return sum + roman_val[s[-1]]

print(romanToInt("III"))            # Expects 3
print(romanToInt("LVIII"))          # Expects 58
print(romanToInt("MCMXCIV"))        # Expects 1994