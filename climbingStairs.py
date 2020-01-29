class Solution(object):
    def __init__(self):
        self.stairs={}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.stairs[0]=1
        self.stairs[1] = 1

        for i in range(2,n+1):
            self.stairs[i]=self.stairs[i-1]+self.stairs[i-2]
        return self.stairs[n]




sol=Solution()
print(sol.climbStairs(5))