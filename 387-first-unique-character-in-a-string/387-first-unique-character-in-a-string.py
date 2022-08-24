class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters={}
        
        for x in range(len(s)):
            if s[x] in letters:
                letters[s[x]]=False
            else:
                letters[s[x]]=True

        
        for x in range(len(s)):
            if letters[s[x]]:
                return x
        
        return -1
        