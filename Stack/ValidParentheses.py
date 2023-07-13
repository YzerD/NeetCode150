# LC 20: Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/

"""
Question:
  Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
  
  An input string is valid if:
  
  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
  Input: s = "()"
  Output: true

Example 2:
  Input: s = "()[]{}"
  Output: true

Example 3:
  Input: s = "(]"
  Output: false
 

Constraints:
  1 <= s.length <= 104
  s consists of parentheses only '()[]{}'.
  
U-nderstand:
  - What is the input?
      The input is a string containing just the characters '(', ')', '{', '}', '[' and ']'.
  - What is the output?
      The output is a boolean value which returns true if the input is valid and false otherwise
  - What is a valid input?
      The problem states the input is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.
  - Can the input string be empty?
      In the constraints of the problem it says the string can range from 1 to 10^4. This means
      the edge case is of 1 and it must be an invalid input since there needs to be at least 2
      character in a string to make a valid input.
  - Can there be other characters besides parentheses in the string?
      No, The problem states that the input string consists of parentheses only '()[]{}'


  Happy Case:
  Input: s = "({[]})"
  Output: True

  Edge Case:
  Input: s = "("
  Output: False

M-atch:
  "TIP102 - UNIT 1 Session 2 Slides: "
    Stack: What could we push onto a stack to make this problem easier? Stacks don’t allow us to keep track of data based on keys.
    
  Queue: Queues fall into the same category as Stacks, do we need to maintain any sense of ordering to solve this problem?
  
  HashMap: HashMaps allow us to store data for quick access. What could we store in a HashMap to make this problem easier?
  
  Heap: Do we need some sort of ordering to our data that a Heap could provide?


  I think we can utilize a stack to solve this problem. Iterating over the length of the string, we can push onto the stack open parentheses and then check if the character is the appropriate closing parentheses and that the stack isn't empty, if this checks out we pop the stack. After iterating through the array return not stack to signify that it's empty. 
  
P-lan:
  1) Create our stack
  2) Iterating over the string
  3) If the char is an open parentheses, push it onto the stack
  4) If the char is a closed parenetheses, if the stack isn't empty,
     and on the top of the stack is the matching open parentheses, pop the stack
  5) After processing the string, return not stack signifing it's empty


I-mplement:
"""
def isValid(s: str) -> bool:
    # Create our stack
    stack = []

    # Iterating over the length of the string
    for i in range(len(s)):
        # If the character is an open parentheses
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            # Push it onto the stack
            stack.append(s[i])

        # If the character is ')'
        elif s[i] == ')':
            # And the top of the stack isn't empty and has the matching character
            if stack and stack[-1] == '(':
                # Pop the stack
                stack.pop()
            # Otherwise, it's not matching and is unbalanced
            else:
                return False

        # Repeat the checks for ']' and '}'
        elif s[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
                
        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return False

    # Return not stack (True if it's empty and False if it's not)
    return not stack

"""
R-eview:
  At first I ran into trouble with the test cases, the one's where the input is valid. It took a while but I realized that in checking the top of the stack, I had it to s[-1] instead of stack[-1]. Which means that I was checking the end of the string rather than the top of the stack. After fixing that error, the program passes.

  Ran into another issue, it was saying list was out of index in the logic statements when checking the stack. I then realized it should be swapped over with checking the top of the stack. So it would check if there's something in the stack first before checking the top of it.
"""

# Expects True
paren1 = "()"
print("Test 1: ", paren1)
print(isValid(paren1), "\n")

# Expects True
paren2 = "()[]{}"
print("Test 2: ", paren2)
print(isValid(paren2), "\n")

# Expects False
paren3 = "(]"
print("Test 3: ", paren3)
print(isValid(paren3))