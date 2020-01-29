class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def findFirst(nums,target):
            start=0
            end=len(nums)-1

            while start+1<end:
                mid = int(start + (end - start) / 2)
                if nums[mid]<target:
                    start=mid
                else:
                    end=mid

            if nums[start]==target:return start
            if nums[end]== target: return end
            return -1

        def findLast(nums, target):
            start = 0
            end = len(nums) - 1

            while start + 1 < end:
                mid = int(start + (end - start) / 2)
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid

            if nums[start] == target: return start
            if nums[end] == target: return end
            return -1


        start=findFirst(nums,target)
        if start==-1:
            return [-1.-1]
        end=findLast(nums,target)
        return [start,end]

sol=Solution()
print(sol.searchRange([1,2,3,4,8,8,8,8,9],8))