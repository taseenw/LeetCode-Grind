class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters={}
        
        for x in range(len(s)):
            if s[x] in letters:
                letters[s[x]]+=1
            else:
                letters[s[x]]=1
        
        for x in range(len(s)):
            if letters[s[x]] == 1:
                return x
        
        return -1
        