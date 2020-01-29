class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        first=0
        last=len(matrix[first])-1
        print(last)
        while first<last:
            temp=matrix[first]
            matrix[first]=matrix[last]
            matrix[last]=temp
            first+=1
            last-=1

        for i in range(last+1):
            for j in range(i+1,len(matrix)):
                print(j)
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp

        print(matrix)

sol=Solution()
m=[
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
sol.rotate(m)