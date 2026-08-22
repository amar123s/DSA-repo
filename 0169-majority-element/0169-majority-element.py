class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=dict()
        for ele in nums:
            freq[ele]=freq.get(ele,0)+1
        maxx=0
        ans=None
        for ele in nums:
            if freq[ele]>maxx:
                maxx=freq[ele]
                ans=ele
        return ans

        