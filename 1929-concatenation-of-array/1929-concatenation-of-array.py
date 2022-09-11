class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        ans=[]
        it=True
        x=0
        while x < n:
            ans.append(nums[x])
            x+=1
            if x == n and it:
                it=False
                x=0
                
        return ans
        