class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count={}


        for i in nums:
            if i in count.keys():
                count[i]+=1
            else:
                count[i]=1

        val=max(count.values())
        for k,v in count.items():
            if v==val:
                return k

