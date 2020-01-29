class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])

        nums[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):

            nums[i]=max(nums[i-1],nums[i-2]+nums[i])

        return nums[len(nums)-1]
    