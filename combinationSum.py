class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans=[]
        candidates=sorted(candidates)
        print(candidates)
        def sum(nums,curr_sum,curr_set):
            for i in range(len(nums)):
                temp_sum=nums[i]+curr_sum
                if temp_sum==target:
                    ans.append(curr_set+[nums[i]])
                elif temp_sum>target:
                    return
                else:
                    sum(nums[i:],temp_sum,curr_set+[nums[i]])

        sum(candidates,0,[])

        return ans

sol=Solution()
print(sol.combinationSum([2,3,5,4],8))