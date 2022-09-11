class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        s=set(jewels)
        for x in range(len(stones)):
            if stones[x] in s:
                count+=1
        return count
        