class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums)==1:
            return True

        if not nums:
            return False

        validi=len(nums)-1
        i=len(nums)-2

        while i>=0:

            if nums[i]>=validi-i:
                validi=i

            i=i-1

        return validi==0
