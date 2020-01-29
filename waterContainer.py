class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        end=len(height)-1
        max_ar=0

        while start<end:
            length=end-start
            width=min(height[start],height[end])
            area=length*width

            if area>max_ar:
                max_ar=area

            if height[start]>height[end]:
                end-=1
            else:
                start+=1

        return max_ar