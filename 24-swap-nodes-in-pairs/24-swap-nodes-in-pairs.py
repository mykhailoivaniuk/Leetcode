# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        
        cur = head

        while cur is not None and cur.next is not None:
            #initialize
            start = cur
            end = cur.next
        
            #advance
            cur = cur.next.next
            
            #switch pointers in the pair
            start.next = end.next
            end.next = start
            
            #connect to the list
            prev.next = end
            prev = start
            

            
        
        return dummy.next
        