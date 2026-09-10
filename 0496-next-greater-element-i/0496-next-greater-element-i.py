class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        grater={}
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1] <=nums2[i]:
                stack.pop()
            
            if stack:
                grater[nums2[i]]=stack[-1]
            else:
                grater[nums2[i]]=-1
            
            stack.append(nums2[i])
        
        answer=[]
        for num in nums1:
            answer.append(grater[num])
        
        return answer
