class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        oldcolor=image[sr][sc]
        if oldcolor==color:
            return image
        n=len(image)
        m=len(image[0])
        def dfs(i,j):
            if i<0 or i>=n or j<0 or j>=m:
                return
            if image[i][j]!=oldcolor:
                return
            
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        dfs(sr,sc)
        return image

        