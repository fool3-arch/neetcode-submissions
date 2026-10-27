class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        for i in matrix:
            if i[0]<=target<=i[-1]:
                l=0
                r=n-1
                while l<=r:
                    m=(l+r)//2
                    if i[m]<target:
                        l=m+1
                    elif i[m]>target:
                        r=m-1
                    else:
                        return True
                return False
        return False
