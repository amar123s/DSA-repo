# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy=ListNode(0)
        dummy.next=head
        group_prev=dummy

        while True:
            kth=group_prev
            for i in range(2):
                kth=kth.next

                if not kth:
                    return dummy.next
            
            first=group_prev.next
            second=first.next

            first.next=second.next
            second.next=first
            group_prev.next=second

            group_prev=first

        
