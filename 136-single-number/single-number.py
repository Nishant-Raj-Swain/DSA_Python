class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ele = 0
        for i in range(0,len(nums)):
            ele = nums[i]^ele

        return ele

        
        