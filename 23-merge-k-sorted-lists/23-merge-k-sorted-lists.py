# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Possible override of compare methods
        # ListNode.__eq__ = lambda self, other: self.val == other.val
        # ListNode.__lt__ = lambda self, other: self.val < other.val
        
        cur_nodes = []
        for i in range(len(lists)):
            if lists[i]:
                # Need to store 3tuple with entry num to break ties
                # or override __eq__ and __lt__ methods
                heappush(cur_nodes, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        cur = dummy
        while cur_nodes:
            _, _, cur_node = heappop(cur_nodes)
            cur.next = cur_node
            cur = cur.next
            if cur_node.next:
                i += 1
                heappush(cur_nodes, (cur_node.next.val, i, cur_node.next))
        
        return dummy.next
            
        
        
        