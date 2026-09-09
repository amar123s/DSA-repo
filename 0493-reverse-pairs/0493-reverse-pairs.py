class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesor(arr,start,end):
            if end -start <=1:
                return 0
            mid = (start+end)//2
            count = mergesor(arr,start,mid)+mergesor(arr,mid,end)
            j=mid
            for i in range(start,mid):
                while j < end and arr[i]> nums[j]*2:
                    j+=1
                count += j- mid
            arr[start:end]= sorted(arr[start:end])
            return count
        return mergesor(nums,0,len(nums))

        