# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        l = r = head
        count = 0
        prevGroup = dummy
        
        while True:
            while r is not None and count < k:
                r = r.next
                count += 1
            if count == k:
                count = 0 
                prev, cur = r, l
                for _ in range(k):
                    next = cur.next
                    cur.next = prev
                    prev = cur
                    cur = next
                
                prevGroup.next = prev
                prevGroup = l
                l = r
                
            else:
                return dummy.next
            
        