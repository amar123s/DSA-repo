class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        SETT=set(nums)
        maxx=0

        for num in SETT:
            if num-1 not in SETT:
                count=1

                while num+count in SETT:
                    count+=1
                maxx=max(maxx,count)
        return maxx