class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        minB = prices[0]
        for x in range(1, len(prices)):
            if prices[x] < minB:
                minB = prices[x]
            else:
                newDiff = prices[x] - minB
                if newDiff > maxP:
                    maxP = newDiff
        return maxP
