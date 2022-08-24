class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runSum=0
        newList=[]
        for x in range(len(nums)):
            runSum+=nums[x]
            newList.append(runSum)
        
        return newList