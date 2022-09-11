class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        bsum=0
        for x in range(len(accounts)):
            csum=sum(accounts[x])
            if csum >= bsum:
                bsum=csum
        return bsum