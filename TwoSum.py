#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i,num in enumerate(nums):
            rem=target-num
            if rem in nums and nums.index(rem)!=i:
                return [i,nums.index(rem)]



sol=Solution()


print(sol.twoSum([2, 7, 11, 15],9))
