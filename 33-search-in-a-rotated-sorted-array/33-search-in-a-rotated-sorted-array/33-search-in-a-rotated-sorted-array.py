class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) //2
            if nums[mid] == target:
                return mid
            #L to M is left sort if this is true
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #Right
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1            
                else:
                    l = mid + 1

        return -1

            