class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output=[]
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            #While deque not empty, and the value in the queue is smaller than what's coming in (-1 is last)
            while q and nums[q[-1]] < nums[r]:
                #Pop em all
                q.pop()
            
            q.append(r)

            #If left in array is bigger than (outside bounds, l is more right than q) our first queue, pop the left in the queue
            if l > q[0]:
                q.popleft()
            
            #Window hit, append left most (rememeber the queue stores indecies)
            if r + 1 >= k:
                output.append(nums[q[0]])
                #You only increment left, once the window has hit k, r is touching the elements, left is bound
                l+=1
            r+=1
        
        return output