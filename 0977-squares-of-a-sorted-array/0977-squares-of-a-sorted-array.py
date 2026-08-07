class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=0
        right=n-1
        i=n-1
        squared=[0]*n
        while left<=right:
            if nums[left]*nums[left]> nums[right]*nums[right]:
                squared[i]=nums[left]*nums[left]
                left+=1
            else:
                squared[i]=nums[right]*nums[right]
                right-=1
            i-=1
        return squared
