class Solution(object):
    def getConcatenation(self, nums):
        n=len(nums)
        hmap={}
        ans=[]
        
        for x in range(n):
            hmap[x]=nums[x]
            ans.append(hmap[x])
            
        for x in range(n):
            ans.append(hmap[x])
        
        return ans
        