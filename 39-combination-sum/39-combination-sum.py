class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        #Recursive dfs
        def dfs(i, cur, total):
            if total == target:
                #Create copy since we are gonna continue to use this
                res.append(list(cur))
                return
            #No combo
            if i >= len(candidates) or total > target:
                return
            
            #Decision to add this candidate
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])

            #Not include this
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)

        return res