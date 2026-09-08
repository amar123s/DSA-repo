class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        total=sum(nums)
        left=0
        for i in range(n):
           rightu=total-left-nums[i] 
           if left==rightu:
            return i
           left+=nums[i]
        return -1
        
        