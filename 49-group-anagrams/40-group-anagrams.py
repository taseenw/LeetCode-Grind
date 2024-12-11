class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Initialize like this since key might not exist yet, avoid if key not in res, res[key] = [], res[key].append(value), one step
        res=defaultdict(list)
        outputArr=[]
        for string in strs:
            #each string has its own
            count = [0] * 26

            for c in string:
                #any asci value minus a will give its value from 0 (a 65, b 66 -> 1) for index
                count[ord(c) - ord("a")] +=1

            #string as value to the count arr, dictionary keys must be immutable, so we convert to tuple
            res[tuple(count)].append(string)

        return res.values()


