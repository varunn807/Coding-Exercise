class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        if len(s) == 1 or s[0] in ')]}': return False
        stack=[]
        print(s)
        for i in s:
            print(i)
            if i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            elif i == '[':
                stack.append(']')
            elif len(stack)==0 or stack.pop()!=i:
                    return False

        return len(stack)==0
sol=Solution()
print(sol.isValid("(("))