class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        for x in range(1,len(nums)):
            if nums[x]!=nums[x-1]:
                nums[k]=nums[x]
                k+=1
        
        return k