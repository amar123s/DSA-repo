class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        max_end=nums[0]
        min_end=nums[0]
        maxsofar=nums[0]
        for i in range(1,n):
            curr=nums[i]
            temp_max=max(curr,max_end*curr,min_end*curr)
            min_end=min(curr,max_end*curr,min_end*curr)
            max_end=temp_max
            maxsofar=max(maxsofar,max_end)
        return maxsofar

        