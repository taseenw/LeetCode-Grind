class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        un=nums[0]
        for x in range(1,len(nums)):
            if nums[x]!=un:
                nums[k]=nums[x]
                un=nums[k]
                k+=1
        
        return k