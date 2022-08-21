class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        l=0
        for x in range(len(nums)):
            if nums[x]!=0:
                nums[l],nums[x]=nums[x],nums[l]
                l+=1
                
            
                