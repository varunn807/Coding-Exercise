class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        result=nums[0]
        subsum=nums[0]
        i=1

        if not nums:
            return 0

        while i <= len(nums):
            item=nums[i]
            temp=item+subsum
            if temp>item:
                subsum=temp
            else:
                subsum=item
            if subsum>result:
                result=subsum

            i=i+1

        return result