class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newList = []
        
        for x in range(len(nums)):
            newList.append(nums[nums[x]])
            
        return newList