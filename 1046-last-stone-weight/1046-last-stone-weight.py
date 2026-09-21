class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        ans=[-stone for stone in stones]
        heapq.heapify(ans)
        while len(ans)>1:
            y=-heapq.heappop(ans)
            x=-heapq.heappop(ans)
    
            if x!=y:
                heapq.heappush(ans,-(y-x))
        if ans:
            return -ans[0]
        
        return 0
        

        