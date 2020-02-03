class Solution(object):

    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common_prefix = ""
        for i in range(0, len(strs[1])):
            pass


solution = Solution()
strs = ["ddscadc", "asdefev", "adevdf"]
solution.longest_common_prefix(strs=strs)

print(strs[1][::-1])
