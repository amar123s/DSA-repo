class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for length in range(1,amount+1):
            for coin in coins:
                if coin <=length:
                    dp[length]=min(dp[length],1+dp[length-coin])
        
        if dp[amount]==amount+1:
            return -1
        return dp[amount]
        