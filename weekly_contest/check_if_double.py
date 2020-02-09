# Given an array arr of integers, check if there exists two integers N and M such that N is the double of M
# ( i.e. N = 2 * M).


class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for element in arr:
            if 2 * element in arr:
                if element == 0 and arr.count(element) == 1:
                    continue
                return True

        return False


Solution().checkIfExist([-2,0,10,-19,4,6,-8])
