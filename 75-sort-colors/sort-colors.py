class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i,j,k,=0,0,0
        for m in range(0,len(nums)):
            if(nums[m] == 0):
                i+=1
             
            if(nums[m] == 1):
                j+=1
             
            if(nums[m] == 2):
                k+=1

        
        if i > 0 and i<len(nums):
            for m in range(i):
                nums[m] = 0
        
        if j > 0 and (j+i)<=len(nums):
            for m in range(i,(j+i)):
                nums[m] = 1

        if k > 0 and (k+i+j)<=len(nums):
            for m in range((j+i),(k+i+j)):
                nums[m] = 2
        
        #return nums
        


        