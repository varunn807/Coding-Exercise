class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start,end=-1,-1
        for i in range(len(intervals)):
            start=intervals[i][0]
            end = intervals[i][1]
            for j in range(i+1,len(intervals)):
                if intervals[j][0]>=start and intervals[j][1]<=end:
                    continue
                elif intervals[j][0]>=start and intervals[j][1]<=end:


