# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        greater=ListNode(0)
        lesser=ListNode(0)
        curr=head
        lesser_tail=lesser
        greater_tail=greater
        while curr:
            if curr.val <x:
                lesser_tail.next=curr
                lesser_tail=curr
            else:
                greater_tail.next=curr
                greater_tail=curr
            
            curr=curr.next
        
        greater_tail.next=None
        lesser_tail.next=greater.next

        return lesser.next

