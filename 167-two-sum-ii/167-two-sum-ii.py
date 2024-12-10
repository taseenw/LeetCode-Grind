class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        l,r = 0, len(numbers)-1

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r-=1
            if curSum < target:
                l+=1
            if curSum == target:
                return [l+1, r+1]