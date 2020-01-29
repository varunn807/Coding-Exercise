class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count=0

        for i in nums:
            print(i)
            if i==0:

                count+=1
            print("-->",nums)
        for _ in range(count):
            nums.remove(0)
            nums.append(0)

        print(nums)

sol=Solution()
sol.moveZeroes([0,0,1])