class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        d={}
        arr=[]
        for w in strs:
            res.append("".join(sorted(w)))

        for i in range(len(strs)):
            a=res[i]
            if res[i] not in d:
                d[res[i]]=[strs[i]]
            else:
                d[res[i]]+=[strs[i]]

        for k,v in d.items():
            arr.append(v)
        return arr
sol=Solution()
print(sol.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))
