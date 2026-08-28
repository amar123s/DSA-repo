class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum=sum(nums)
        target=totalsum//2
        n=len(nums)
        if totalsum%2!=0:
            return False
        dp=[[False]*(target+1)for _ in range(n+1)]
        dp[0][0]=True
        for i in range(1,n+1):
            for j in range(target+1):
                notpick= dp[i-1][j]
                pick=False
                if nums[i-1] <=j:
                    pick=dp[i-1][j-nums[i-1]]
                dp[i][j]= pick or notpick
        return dp[n][target]
