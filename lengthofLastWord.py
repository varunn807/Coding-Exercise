class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        dummy=s
        res=0
        words=[]
        if dummy.replace(' ',"")=='':
            return 0

        splits=s.split(' ')
        for word in splits:
            if word.replace(" ","")!="":
                words.append(word.replace(" ",""))
        print(words)
        last=len(words)
        if last>=1:
            if len(words[last-1])!=0:
                res=len(words[last-1])
            else:
                res=len(words[last-2])
        return(res)


sol=Solution()
print(sol.lengthOfLastWord("  day"))