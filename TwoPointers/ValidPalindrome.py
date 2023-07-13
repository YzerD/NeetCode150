# LC 125: Valid Palindrome (Easy)
# https://leetcode.com/problems/valid-palindrome/

"""
Question:
  A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
  
  Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
  Input: s = "A man, a plan, a canal: Panama"
  Output: true
  Explanation: "amanaplanacanalpanama" is a palindrome.
  
Example 2:
  Input: s = "race a car"
  Output: false
  Explanation: "raceacar" is not a palindrome.
  
Example 3:
  Input: s = " "
  Output: true
  Explanation: s is an empty string "" after removing non-alphanumeric characters.
  Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints:
  1 <= s.length <= 2 * 105
  s consists only of printable ASCII characters.
  

U-nderstand:
  - Do we need to make all the characters lowercase?
      Yes, the problem states that we need to convert all characters from uppercase to lowercase
  - We need to remove all alphanumeric characters
      This includes, spaces and puncutation
  - What about the empty string?
      If the string is empty, it reads the same forward and backwards, and therefore is a palindrome
      and we would return true
  - What is a palindrome? 
      A palindrome is a string that is read front and back the same way
  

M-atch:
  For arrays and strings, common solution patterns include:
    - Sort
    - Two Pointer Solution
    - Storing the elements of the array in a HashMap or a Set
    - Traversing the array with a sliding window

  Sorting the string wouldn't help us reach a solution. Storing the elements in a hash map or
  set also wouldn't help since we aren't interested in a character's frequency. I think we can 
  use Two Pointers, where we have a left pointer at the beginnging of the string, and the end
  pointer at the end of the string. While the two pointers haven't cross 

P-lan:
  1) Convert string into all lowercase
  2) Iterating over the string, create a new string that consists of just alphanumeric characters
  3) Declare our two pointers at the beginning and end of the string
  4) While our two pointers haven't crossed
  5) Check if our left and right pointers have the same character
     If they don't have the same character we would return false
  6) Iterate our pointers
  7) return True
  
  new string  = s.isalnum() 

I-mplement:

"""

def isPalindrome(s: str) -> bool:
    # Convert string to all lowercase
    s = s.lower()

    # Create our new string variable
    new_string = ""

    # Iterating over all the characters in s
    for i in s:
        # If the character is alphanumeric
        if i.isalnum():
            # Append it to the new string
            new_string += i

    # Declare our two pointers for our new string
    left = 0
    right = len(new_string) - 1

    # While our two pointers haven't crossed
    while left < right:
        # Check if their characters are equal
        if new_string[left] != new_string[right]:
            return False

        # Increment our pointers
        left += 1
        right -= 1

    return True

# Expects True
string1 = "A man, a plan, a canal: Panama"
print("String 1: ", string1)
print(isPalindrome(string1), "\n")


# Expects False
string2 = "race a car"
print("String 2: ", string2)
print(isPalindrome(string2), "\n")


# Expects True
string3 = ""
print("String 3: ", string3)
print(isPalindrome(string3))

