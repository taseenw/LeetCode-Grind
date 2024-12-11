class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = two = 1
        for x in range(n-1):
            #one will be sum of last two
            #two is prev one, we need to hold in temp tho
            temp = one
            one = one + two
            two = temp
        return one