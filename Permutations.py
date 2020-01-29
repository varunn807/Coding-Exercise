class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None or len(nums)==1:
            return nums
        res=[]
        def permu(numList,curr_set):
            if len(curr_set)==len(numList):
                res.append(curr_set)
                return
            else:
                for i in range(len(nums)):
                    if nums[i] not in curr_set:
                        permu(nums,curr_set+[nums[i]])


        permu(nums,[])
        return res

sol=Solution()
print(sol.permute([1,2,3]))

