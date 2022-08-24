class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum=0
        for x in range(len(nums)):
            runSum+=nums[x]
            nums[x]=runSum
        
        return nums