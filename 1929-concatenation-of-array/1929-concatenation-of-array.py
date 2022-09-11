class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        
        for x in range (n):
            nums.append(nums[x])
        
        return nums
        