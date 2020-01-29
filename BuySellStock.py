class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minPrice=prices[0]
        maxP=0

        for i in range(1,len(prices)):
            if prices[i]<minPrice:
                minPrice=prices[i]
            else:
                if prices[i]-minPrice>maxP:
                    maxP=prices[i]-minPrice


        return maxP

