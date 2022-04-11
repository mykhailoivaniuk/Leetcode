# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def getLength(head):
            ll_length = 0
            cur = head
            while cur is not None:
                cur = cur.next
                ll_length += 1
            
            return ll_length
        
        length1 = getLength(headA)
        length2 = getLength(headB)
        
        if length1 > length2:
            longer, shorter  = headA, headB
            diff = length1 - length2
        else:
            longer, shorter = headB, headA
            diff = length2 - length1
            
        while diff > 0:
            longer = longer.next
            diff -= 1
            
        while longer is not None:
            if shorter == longer:
                return shorter
            longer = longer.next
            shorter = shorter.next
        
        return None
        
        