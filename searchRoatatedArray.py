class Solution(object):



    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start=0
        end=len(nums)-1
        if not nums:
            return -1

        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1

        pivot=self.findPivot(nums,start,end)
        print(pivot)


        result=self.binarySearch(nums,start,pivot-1,target)
        if result!=-1:
            return result
        else:
            result=self.binarySearch(nums,pivot,end,target)
            return result

    def findPivot(self, nums, start, end):

        if (nums[0] < nums[len(nums)-1]):
            return 0


        while (start<=end):
            mid=int(start + (end-start)/2)
            print(mid,start,end)
            if(mid<=end and nums[mid]>nums[mid+1]):
                return mid+1
            elif(nums[start]<=nums[mid]):
                start = mid + 1

            else:
                end = mid - 1

    def binarySearch(self,nums,start,end,target):

        if(start>end):
            return -1

        if(start==end):
            if nums[start]!=target:
                return -1
            else:
                return start

        mid=int(start + (end-start)/2)
        print(mid)

        while(start<=end):
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                return self.binarySearch(nums,mid+1,end,target)
            else:
                return self.binarySearch(nums,start,mid-1,target)

sol=Solution()
sol.search([5,1,3],0)