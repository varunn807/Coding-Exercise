class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currList=[]
        i=0
        currMax=0
        while i < len(s):
            if currList.__contains__(s[i]):
                print(currMax)
                if len(currList)>currMax:
                    currMax=len(currList)
                    print(currList)
                    currList=[]
                    continue
            print(s[i])
            currList.append(s[i])
            print("->",currList)


            i=i+1
        return currMax

sol=Solution()
s="abcabcbb"
print(sol.lengthOfLongestSubstring(s))