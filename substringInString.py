class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        pos=haystack.split(needle)[0].__len__()

        if haystack.split(needle)[0].__len__()!=len(haystack):
            return pos
        else:
            return -1

sol=Solution()
print(sol.strStr("mississippi","ab"))
"mississippi"
"issip"
