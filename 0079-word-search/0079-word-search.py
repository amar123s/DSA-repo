class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if r<0 or r>=n or c<0 or c>=m:
                return False
            if board[r][c]!= word[idx]:
                return False
            temp=board[r][c]
            board[r][c]="#"
            found=(dfs(r+1,c,idx+1) or dfs(r-1,c,idx+1) or dfs(r,c+1,idx+1) or dfs(r,c-1,idx+1))

            board[r][c] = temp

            return found
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                     return True
        return False