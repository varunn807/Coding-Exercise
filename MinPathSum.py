class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        sumG=[[0 for i in range(n)] for j in range(m)]

        sumG[0][0]=1

        for i in range(1,m):
            sumG[i][0]=sumG[i-1][0]+grid[i][0]

        for i in range(1,n):
            sumG[0][i]=sumG[0][i-1]+grid[0][i]

        # for i in range(m):
        #     sumG[i][0]=sumG[i][0]+grid[i][0]


        for i in range(1,m):
            for j in range(1,n):
                sumG[i][j]=grid[i][j]+min(sumG[i-1][j],sumG[i][j-1])

        return sumG[m - 1][n - 1]

sol=Solution()
a=[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(sol.minPathSum(a))