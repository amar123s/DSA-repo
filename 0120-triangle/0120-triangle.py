class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[[0 for _ in range(len(triangle[i]))]for i in range(n)]

        for j in range(len(triangle[n-1])):
            dp[n-1][j]=triangle[n-1][j]
        
        for i in range(n-2,-1,-1):
            for j in range(len(triangle[i])):
                down=dp[i+1][j]
                dia=dp[i+1][j+1]
                dp[i][j]=triangle[i][j]+min(down,dia)
        return dp[0][0]
        