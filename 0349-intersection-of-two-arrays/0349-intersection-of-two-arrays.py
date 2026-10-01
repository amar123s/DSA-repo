class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n=len(nums1)
        m=len(nums2)
        res=[]
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j]:
                    if nums1[i] not in res:
                        res.append(nums1[i])
        return res

        