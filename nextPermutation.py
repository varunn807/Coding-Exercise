class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=None

        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                pos=i

        if pos is None:
            nums.sort()
            return nums

        for i in range(len(nums),pos-1,-1):
            if nums[i]>nums[pos-1]:
                temp=nums[pos-1]
                nums[pos-1]=nums[i]
                nums[i]=temp
                break

        nums[pos:]=nums[pos:].sort()
        return nums


