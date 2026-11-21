class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        def backtrack(path,used):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                
                used.add(i)
                path.append(nums[i])

                backtrack(path,used)

                path.pop()
                used.remove(i)

        backtrack([],set())

        return ans
