class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # grid=[[0]*m]*n
        grid=[[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            grid[i][0]=1

        for b in range(n):

            grid[0][b]=1

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]=grid[i-1][j]+grid[i][j-1]


        return grid[m-1][n-1]






sol=Solution()
print(sol.uniquePaths(3,2))