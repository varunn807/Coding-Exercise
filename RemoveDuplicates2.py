class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0 or len(nums)==1 or len(nums)==2:
            return len(nums)
        count=0
        prev=None
        flag=0
        i=0
        while i<(len(nums)):
            if nums[i]!=prev:
                count+=1
                prev=nums[i]
                flag=1
            else:
                if flag<2:
                    flag+=1
                    count+=1
                else:
                    del nums[i]
                    i-=1
            i+=1

        return nums

sol=Solution()
print(sol.removeDuplicates([1,1,1,2,2,3]))
