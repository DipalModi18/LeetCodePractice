class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        reverse = 0
        while x > 0:
            reverse = (reverse * 10) + (x % 10)
            x /= 10
        print(x)
        print(reverse)
        if reverse == temp:
            return True
        else:
            return False


Solution().isPalindrome(121)
