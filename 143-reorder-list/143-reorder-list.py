# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        while head != None:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    def getMidddle(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        return slow
                
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
    
        if head is None or head.next is None:
            return None
        
        dummy = ListNode(0)
        cur = dummy
        
        middle = self.getMidddle(head)

        # reverses list from the middle onwards
        # returns pointer to the last node
        endPtr = self.reverseList(middle)
        startPtr = head
    

        # More elegant list reversal
        # Instead of having smth in the middle
        # Point them to each other instead
        while endPtr.next:
            startPtr.next, startPtr = endPtr, startPtr.next
            endPtr.next, endPtr = startPtr, endPtr.next

        
        return dummy.next
        
        