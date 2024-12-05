class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        for x in range(0, len(prices)-1):
            if prices[x] < prices[x+1]:
                maxP += prices[x+1] - prices[x]
        return maxP