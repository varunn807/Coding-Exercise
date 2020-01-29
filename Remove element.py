class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curr=0
        index=0
        i=0
        while True:
            try:

                if nums[i]==val:
                    nums.pop(i)
                else:
                    i+=1
            except:
                break

        return nums


sol=Solution()
print(sol.removeElement([0,1,2,2,2,3,0,4,2],2))
