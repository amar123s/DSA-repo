class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        m=len(matrix[0])
        low=matrix[0][0]
        high=matrix[n-1][m-1]
        while low < high:
            mid =(low+high)//2
            count=0
            for row in matrix:
                left=0
                right=n-1
                while left <=right:
                    m=(left+right)//2
                    if row[m]<=mid:
                        left=m+1
                    else:
                        right=m-1
                count +=left
            
            if count <k:
                low=mid+1
            else:
                high=mid
        return low

            
