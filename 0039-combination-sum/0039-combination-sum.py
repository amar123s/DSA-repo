class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        curr=[]

        def backtrack(start,total):
            if total == target:
                ans.append(curr.copy())
                return
            
            if total> target:
                return
            
            for i in range(start,len(candidates)):
                curr.append(candidates[i])
                backtrack(i,total+candidates[i])
                curr.pop()
        
        backtrack(0,0)

        return ans