# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersection(self, head):
        fast = head
        slow = head
        contains_cycle = 0
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return fast
        
        return None
        
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return None

        intersection = self.getIntersection(head)
        if intersection is None:
            return None
        
        first, second = head, intersection
        
        while first != second:
            first = first.next
            second = second.next
        
        return first
        
        
        
        
        
        
        