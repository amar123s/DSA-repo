class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        summ=0
        prefix={0:1}
        for num in nums:
            summ+=num
            if summ-k in prefix:
                count+= prefix[summ-k]
            if summ in prefix:
                prefix[summ]+=1
            else:
                prefix[summ]=1
        return count
        