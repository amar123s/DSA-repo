# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist=ListNode(-1)
        dummy=newlist
        i=list1
        j=list2
        while i != None and j != None:
            if i.val < j.val:
                dummy.next=i
                i=i.next
            else:
                dummy.next=j
                j=j.next

            dummy.next.next=None
            dummy=dummy.next
            
        if j != None:
            dummy.next=j
        if i != None:
            dummy.next=i
        result=newlist.next
        return result
        
        