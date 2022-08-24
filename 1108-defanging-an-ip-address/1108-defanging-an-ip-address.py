class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged=""
        for x in range(len(address)):
            if address[x]==".":
                defanged+="[.]"
            else:
                defanged+=address[x]
        
        return defanged