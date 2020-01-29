class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        size=len(nums)
        ls=0
        rs=sum(nums)-nums[0]
        i=0
        total=sum(nums)
        pivot=-1

        if size<1:
            return
        for i in range(size):
            print(ls,rs)
            if ls==rs:
                pivot=i
                break
            else:
                ls=ls+nums[i]
                if i==size-1:
                    rs=0
                else:
                    rs=rs-nums[i+1]
            i=i+1


        return pivot





sol=Solution()
print(sol.pivotIndex([-1,-1,-1,-1,-1,-1]))