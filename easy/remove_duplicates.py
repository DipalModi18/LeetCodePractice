class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
            else:
                i = i + 1
        return len(nums)


Solution().removeDuplicates(nums=[1, 2, 3, 3, 4, 4, 5, 5, 5])

