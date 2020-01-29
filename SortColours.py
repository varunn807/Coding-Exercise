class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        start=0
        end=len(nums)-1

        def swap(a,b,arr):
            arr[a],arr[b]=arr[b],arr[a]
        i=0

        while i <end+1:

            if nums[i]==0:
                nums[i], nums[start] = nums[start], nums[i]

                start+=1
            elif nums[i]==2:
                nums[i], nums[end] = nums[end], nums[i]
                end-=1
                i-=1
            i+=1


sol=Solution()
sol.sortColors( [2,0,2,1,1,0])