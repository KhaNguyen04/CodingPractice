# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        res=start=ListNode(next=head)
        prev=head
        while prev:
            cur=prev.next
            if not cur:
                return res.next
            tmp=cur.next
            cur.next=prev
            prev.next=tmp
            start.next=cur
            start=prev
            prev=tmp
        return res.next