class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            if i<0 or i>=row or j<0 or j>=cols:
                return
            
            if grid[i][j]=="0":
                return
            
            grid[i][j]="0"

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        islands=0
            
        for i in range(row):
            for j in range(cols):
                if grid[i][j]=="1":
                    islands+=1
                    dfs(i,j)
        
        return islands

            



        