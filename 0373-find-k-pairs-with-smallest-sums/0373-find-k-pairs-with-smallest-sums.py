class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        if not nums1 or not nums2 or k ==0:
            return []

        min_heap=[]
        for i in range(min(len(nums1),k)):
            heapq.heappush(min_heap,(nums1[i]+nums2[0],i,0))

        result=[]

        while min_heap and len(result)<k:
            total,i,j=heapq.heappop(min_heap)

            result.append([nums1[i],nums2[j]])
            if j+1 < len(nums2):
                next_j=j+1
                next_sum=nums1[i]+nums2[next_j]

                heapq.heappush(min_heap,(next_sum,i,next_j))
        
        return result
        