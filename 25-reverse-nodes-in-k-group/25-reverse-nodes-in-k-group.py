# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_length(self, head):
        ll_length = 0 
        cur = head
        
        while cur is not None:
            cur = cur.next
            ll_length += 1
            
        return ll_length
    
    def reverse_ll(self,head,k):
        prev = None
        
        # Remember: head of reversed list - last node,
        # end of reversed l - head now
        start = None
        end = head
        
        cur = head
        check = head

        while k > 0 and cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            k -= 1
        
        #prev is the start of the reversed list now
        
        return prev, end, cur
        
        
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0, next = head)
        ll_length = self.get_length(head)
        groups = ll_length // k
        cur = head
        
        prev = dummy

        while cur is not None and cur.next is not None and groups > 0:
            start_of_reverse, end_of_reverse, next_ptr = self.reverse_ll(cur,k)
            prev.next = start_of_reverse
            prev = end_of_reverse
            end_of_reverse.next = next_ptr
            cur = next_ptr
            groups -= 1

        
        return dummy.next
        