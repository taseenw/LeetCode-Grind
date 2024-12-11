class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lower()
        changes = 0
        for c in range(0,len(s)-1):
            if s[c] != s[c+1]:
                changes+=1
        
        return changes