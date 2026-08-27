class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        if n == 0:
            return 0
        dp=[[0]*m for _ in range(n)]
        for j in range(m):
            dp[n-1][j]=matrix[n-1][j]
        for i in range(n-2,-1,-1):
            for j in range(m):
                left=dp[i+1][j-1] if j-1 >=0 else float("inf")
                down=dp[i+1][j]
                right=dp[i+1][j+1] if j+1 <m else float("inf")
                dp[i][j]=matrix[i][j]+min(left,down,right)
        return min(dp[0])

        