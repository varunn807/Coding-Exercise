class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=""
        if s=="":
            return s

        for i,char in enumerate(s):
            #for odd palindrome
            start=i-1
            end=i+1

            while(start>=0 and end<len(s) and s[start] == s[end]):
                if len(s[start:end+1])>len(result):
                    result=s[start:end+1]

                start=start-1
                end=end+1

            #for even palindrome
            start=i
            end=i+1
            while(start>=0 and end<len(s) and s[start] == s[end]):
                if len(s[start:end+1])>len(result):
                    result=s[start:end+1]
                start=start-1
                end=end+1
        if result == "":
            return s[0]
        else:
            return result

sol=Solution()
print(sol.longestPalindrome("ac"))