class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Initial val of 1, using res array for work avoiding extra memory
        res = [1] * len(nums)
        prefix = postfix = 1

        #Prefix from beginning
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]
        #Postfix go from back, multiplying prefix populated by postfix, and new postfix is num ele *prev postfix
        #Python convention...
        for y in range(len(nums)-1, -1, -1):
            res[y] *= postfix
            postfix *=nums[y]
            
        return res