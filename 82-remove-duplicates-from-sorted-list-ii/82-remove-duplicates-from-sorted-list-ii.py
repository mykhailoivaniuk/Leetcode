# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        
        while cur is not None and cur.next is not None:
            ahead = cur.next
            if cur.val == ahead.val:
                # loop until we find non-duplicate or the end of the list
                while ahead is not None and cur.val == ahead.val:
                    ahead = ahead.next
                prev.next = ahead
                
            else:
                prev = cur
            
            cur = ahead
        
        return dummy.next
        