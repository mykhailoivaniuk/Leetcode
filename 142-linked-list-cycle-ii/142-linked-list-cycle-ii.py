# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None
        
        fast = head.next
        slow = head
        contains_cycle = 0
        
        while fast and fast.next:
            if fast == slow:
                contains_cycle = 1
                break
            slow = slow.next
            fast = fast.next.next
        
        if not contains_cycle:
            return None

        cycle_length = 1
        
        cur, fast = slow, slow.next
        while cur != fast:
            fast = fast.next
            cycle_length += 1
        
        first, second = head, head
        
        while cycle_length > 0:
            second = second.next
            cycle_length -= 1
        
        while first != second:
            second = second.next
            first = first.next
            
        return second

        
        
        
        
        
        
        