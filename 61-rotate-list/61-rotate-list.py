# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        list_length = 0
        cur = head
        if head is None or head.next is None:
            return head
        
        while cur.next is not None:
            list_length += 1
            cur = cur.next
        
        list_length += 1
        
        if k == list_length or k == 0:
            return head
        
        cur.next = head
        break_idx = list_length - (k % list_length)
        
        cur = head
        for i in range(1, break_idx):
            cur = cur.next
        
        head = cur.next
        cur.next = None
        
        return head
            
            
        
        