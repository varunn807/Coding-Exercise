class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        compare=strs[0]
        common=""
        x=0
        length=len(strs)
        for i in strs[1:length]:
            while x<len(compare) and x<len(i) and compare[x] == i[x]:
                common=common+compare[x]
                x+=1
            if common=="":
                return ""
            compare=common
            common=""
            x=0

        return compare


sol=Solution()
print(sol.longestCommonPrefix(['flower','flow','flight']))