class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi=sum(accounts[0])
        for i in range(len(accounts)):
            wealth=0
            for j in range(len(accounts[i])):
                wealth+=accounts[i][j]

            if wealth > maxi:
                maxi=wealth
        return maxi

        