# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        slow = head
        fast = head
        
        cur = head
        idx = 1
        # advance fast by k positions ahead of slow
        while idx < k:
            fast = fast.next
            idx += 1
        
        k_start = fast
        
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        
        k_end = slow
        temp = k_start.val
        k_start.val = k_end.val
        k_end.val = temp
        
        return head
        
        
        
        
        