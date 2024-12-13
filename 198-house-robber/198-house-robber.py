class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Just maintain last two maxes we can rob from
        rob1 = rob2 = 0

        for house in nums:
            #Compute maximum we can rob till value house
            temp = max(house + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
        