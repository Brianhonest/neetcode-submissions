# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow , fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev ,curr = None,slow
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        l,r = head,prev
        res = 0
        while r:
            res = max(res,l.val + r.val)
            l = l.next
            r = r.next
        return res