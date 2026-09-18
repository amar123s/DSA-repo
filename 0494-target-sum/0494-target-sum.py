class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo={}
        def helper(idx,summ):
            if (idx,summ) in memo:
                return memo[(idx,summ)]
            if idx == len(nums):
                return 1 if target == summ else 0
            plus= helper(idx+1,summ+nums[idx])
            minus=helper(idx+1,summ-nums[idx])
            memo[(idx,summ)] = plus + minus
            return memo[(idx,summ)]
        return helper(0,0)
        