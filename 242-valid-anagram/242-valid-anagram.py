class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap={}
        tMap={}
        
        if len(s)!=len(t):
            return False
        
        for x in range(len(s)):
            sMap[s[x]]= 1+ sMap.get(s[x],0)
            tMap[t[x]]= 1+ tMap.get(t[x],0)
        
        for key in sMap:
            if sMap[key]!=tMap.get(key,0):
                return False
        
        return True