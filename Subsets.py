class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def permu(res,nums):
            if not nums:
                return res

            final=[]

            for sett in res:
                final.append(sett+[nums[0]])
            return permu(final+res,nums[1:])





        return permu([[]],nums)

sol=Solution()
print(sol.subsets([1,2,3]))