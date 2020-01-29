class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=len(nums1)
        b=len(nums2)

        list=nums1+nums2

        list=sorted(list)

        if (a+b)%2 == 0:
            n=int((a+b)/2)
            print((float(list[n - 1]) + float(list[n]) / 2))
            return((list[n-1]+list[n])/2)
        else:
            n=int((a+b+1)/2)
            return((list[n-1]))



sol=Solution()
print(sol.findMedianSortedArrays([1,2],[3,4]))