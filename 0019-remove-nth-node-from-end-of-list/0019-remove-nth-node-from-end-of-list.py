# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s=head
        f=head
        i=1
        while i <n:
            f=f.next
            i+=1
        prev=None
        while f.next != None:
            prev=s
            f=f.next
            s=s.next
        if prev ==None:
            return head.next
        prev.next=s.next

        return head