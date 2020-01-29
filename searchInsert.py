class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums)==1:
            if nums[0]==target:
                return 0
        start=0
        end=len(nums)-1

        if target>nums[end]:
            return end+1
        if target<=nums[start]:
            return 0



        while True:
            mid = int(start + (end - start) / 2)
            print(mid)
            if nums[mid] == target:
                return mid
            elif target > nums[mid] and target <= nums[mid + 1]:
                return mid + 1
            elif target < nums[mid] and target > nums[mid - 1]:
                if target==nums[mid-1]:
                    return mid-1
                return mid
            elif target > nums[mid]:
                start=mid+1
            elif target < nums[mid]:
                end=mid-1


        # if nums[mid]==target:
        #     return mid
        # elif target>nums[mid] and target<=nums[mid+1]:
        #     return mid+1
        # elif target<nums[mid] and target>=nums[mid-1]:
        #     return mid-1
        # elif target>nums[mid]:
        #     return self.searchInsert(nums[mid+1:end+1],target)
        # elif target<nums[mid]:
        #     return self.binSearch(nums[:mid],target)

sol=Solution()
print(sol.searchInsert([1,3,5,6], 7))