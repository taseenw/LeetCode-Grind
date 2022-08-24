class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X":10, "L": 50, "C":100, "D":500, "M":1000}
        sumc=0
        for c in range(len(s)):
            if c+1 < len(s) and romans[s[c]] < romans[s[c+1]]:
                sumc-=romans[s[c]]
            else:
                sumc+=romans[s[c]]
                
        print(sumc)
        
        return sumc
