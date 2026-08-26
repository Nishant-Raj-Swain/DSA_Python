class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        k=0
        j=1
        i=0
        while i < len(result):
            if nums[i] > 0:
                result[k] = nums[i]
                k+=2
            else:
                result[j] = nums[i]
                j+=2
            
            i+=1

        return result



        