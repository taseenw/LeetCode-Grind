class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for x in range(len(nums)):
            if nums[x]==target or nums[x] > target:
                return x
            elif x==len(nums)-1:
                return len(nums)