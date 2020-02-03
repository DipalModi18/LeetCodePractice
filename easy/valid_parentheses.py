"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = [s[0]]
        for ch in s[1:]:
            if len(stack) == 0:
                stack.append(ch)
                continue
            top_element = stack[len(stack)-1]
            if ch in brackets.keys() and top_element == brackets[ch]:
                stack.pop()
            else:
                stack.append(ch)
        return True if len(stack) == 0 else False


print(Solution().isValid("(([]){})"))
