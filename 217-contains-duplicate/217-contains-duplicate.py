class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ln=len(nums)
        sl=len(set(nums))
        
        if sl!=ln:
            return True
        return False