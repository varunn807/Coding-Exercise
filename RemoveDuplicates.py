class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i=1
        if len(nums)<=1:
            return len(nums)

        while i < len(nums):
            if nums[i]==nums[i-1]:
                nums.pop(i)
            else:
                i+=1




        return nums

sol=Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,5,5,6,7,8]))
#a=[0,0,1,1,1,2,2,3,5,5,6,7,8]
#a.remove(1)
#print(a)