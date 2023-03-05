"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
---------------------------------------------
Example:

    Input: s = "()[]{}"
    Output: true
---------------------------------------------
Ref: https://leetcode.com/problems/valid-parentheses
Tag: Easy

"""
def isValid(s):
    _rev = {')':'(', ']':'[','}':'{'}
    char_stack = []
    
    for c in s:
        if c in _rev:
            if char_stack and char_stack[-1] == _rev[c]:
                char_stack.pop()
            else:
                return False
        else:
            char_stack.append(c)

    return not char_stack

chars = input()
print(isValid(chars))
