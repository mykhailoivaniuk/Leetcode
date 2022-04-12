"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, start: 'Optional[Node]') -> 'Optional[Node]':    
        if start is None:
            return None
        
    
        cur = start
        #Constant Space Solution
        while cur:
            copy_node = Node(cur.val)
            next = cur.next
            
            cur.next = copy_node
            copy_node.next = next
            cur = next
            
        cur = start
        while cur and cur.next:
            #copied_node = cur.next
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = start
        copied_head = cur.next
        prev = None
        while cur and cur.next:
            if prev is not None:
                prev.next = cur.next
            prev = cur.next
            cur.next = cur.next.next
            cur = cur.next           
            
        return copied_head
            
            
            
        
        
        