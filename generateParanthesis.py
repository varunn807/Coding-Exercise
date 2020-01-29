class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]



        def gen(p,q,s):

            if p<0 or q<0:
                return

            if p==0 and q==0:
                ans.append(s)
                print(s)
                return

            if p>q:
                return
            i=s+"("
            j=s+")"

            gen(p-1,q,i)
            gen(p,q-1,j)

        gen(n, n, "")

        return ans

sol=Solution()
print(sol.generateParenthesis(3))