class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=-1
        end=len(nums)-1
        if len(nums)==0:
            return None
        if len(nums)==1:
            return nums
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                if start==-1:
                    start=i-1
                else:
                    end=i

        return end-start+1