class Solution(object):

    def twoSum(self,nums,target):

        for i,num in enumerate(nums):

            rem=target-nums[i]

            if rem in nums and nums.index(rem)!=i:
                return [rem,nums[i]]

        return -1

    def threeSum(self,nums):
        mylist=[]
        flag=0
        count=0
        if 0 in nums:
            flag=1
        for i in range(len(nums)):
            temp=nums
            if nums[i]<0:
                print(nums[i])
                temp.pop(i)
                res=self.twoSum(temp,-nums[i])
                print("--",res)
                if res!=-1:
                    res.append(nums[i])
                    print(res)
                    res.sort()

                    if res not in mylist:
                        mylist.append(res)
                if flag:
                    if -nums[i] in nums:
                        res=[nums[i],0,-nums[i]]
                        if res not in mylist:
                            mylist.append([nums[i],0,-nums[i]])
            if nums[i]==0:
                count=count+1
        if count>=3:
            mylist.append([0,0,0])
        return mylist






sol=Solution()


print(sol.threeSum([1,2,-2,-1]))

