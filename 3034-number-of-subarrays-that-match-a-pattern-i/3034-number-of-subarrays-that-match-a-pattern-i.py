class Solution(object):
    def countMatchingSubarrays(self, nums, pattern):
        # O(N * M) time complexity, where N is the length of nums and M is the length of pattern

        # Helper function to check if a subarray matches the pattern
        def matches(subarray, pattern):
            # Iterate over the pattern to check each condition
            for i in range(len(pattern)):
                # Check if the relationship between subarray elements doesn't match the pattern
                if (pattern[i] == 1 and subarray[i + 1] <= subarray[i]) or \
                   (pattern[i] == 0 and subarray[i + 1] != subarray[i]) or \
                   (pattern[i] == -1 and subarray[i + 1] >= subarray[i]):
                    return False
            return True

        count = 0  # Initialize the count of matching subarrays
        n, m = len(nums), len(pattern)  # Length of nums and pattern

        # Edge case: If nums is too short or pattern is empty, return 0
        if n < m + 1 or m == 0:
            return 0

        # Slide over nums to check all possible subarrays of size m + 1
        for i in range(n - m):
            # Extract subarray and check if it matches the pattern
            #nums[i:i + m + 1] is the subarray of nums from index i to i + m
            if matches(nums[i:i + m + 1], pattern):
                count += 1 

        return count 