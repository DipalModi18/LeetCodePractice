# Minimum Number of Steps to Make Two Strings Anagram
# Given two equal-size strings s and t. In one step you can choose any character of t and replace it with
#   another character.
# Return the minimum number of steps to make t an anagram of s.
# An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        for ch in s:
            if ch in t:
                t = t.replace(ch, '', 1)

        return len(t)


print(Solution().minSteps('bab', 'aba'))

