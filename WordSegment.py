class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        def check(s,wordD):
            w=""
            if len(s)==0:
                return True
            for i in wordD:
                if i in s:
                    w=i
                    break
                if w!="":
                    check(s.replace(w,""),wordD)
                else:
                    return False
