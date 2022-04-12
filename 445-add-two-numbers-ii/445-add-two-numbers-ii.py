# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_ll(self, cur, prev=None):
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if l1 is None or l2 is None:
            return l1 if l1 is not None else l2
            
        head1, head2 = self.reverse_ll(l1), self.reverse_ll(l2)
        carry = 0
        prev = None
        while head1 or head2:
            
            cur_sum = carry
            if head1:
                cur_sum += head1.val
                head1 = head1.next
            if head2:
                cur_sum += head2.val
                head2 = head2.next
                
            cur = ListNode(cur_sum%10)
            
            cur.next = prev
            prev = cur
            
            carry = cur_sum//10
        
        if carry:
            cur = ListNode(carry)
            cur.next = prev
            prev = cur
        
        return prev
            
            
            
            
        