class Solution(object):
    def minCostClimbingStairs(self, cost):

        import math
        minCosts=[None]*(len(cost)+1)
        print(len(minCosts))
        minCosts[0] = 0
        minCosts[1]=0

        for i in range(2,(len(cost)+1)):
            minCosts[i]=min([minCosts[i-1]+cost[i-1] ,minCosts[i-2]+cost[i-2]])

        return minCosts[len(cost)]
        """
        :type cost: List[int]
        :rtype: int
        """

sol=Solution()
print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))