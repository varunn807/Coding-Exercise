import math
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        counter=0
        rev=0
        rem=[]
        minus=False
        if x > (math.pow(2,31)-1) or x < -math.pow(2,31):
            return 0
        if x<0:
            minus=True
            x=-x


        while x > 0:
            rem.insert(0,x%10)
            x=int(x/10)
        for i in range(len(rem)):
            rev=rev+rem[i]*math.pow(10,i)

        if rev > (math.pow(2,31)-1) or rev < -math.pow(2,31):
            return 0

        return int(rev) if not minus else -int(rev)

sol=Solution()
print(math.pow(2,31))
print(sol.reverse(1534236469))