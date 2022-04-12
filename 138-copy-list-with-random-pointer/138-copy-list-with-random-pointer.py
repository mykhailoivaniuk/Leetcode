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
        # store reference to node in hashmap
        # pass once copy usual pointers
        # pass two copy random pointers
        Node.print = lambda self: print(f'{self.val} {self.next}')
        if start is None:
            return None
        
        dummy = Node(0)
        
        node_pointers = {}
        prev = dummy
        idx = 0
        head = start
        
        #Linear Space Solution
        while head:
            copy_node = Node(head.val)
            prev.next = copy_node
            node_pointers[head] = copy_node
            
            prev = copy_node
            head = head.next
            idx += 1
        
        cur = dummy.next
        head = start
        while cur:
            if head.random is not None:
                cur.random = node_pointers[head.random]
            else:
                cur.random = None
            cur = cur.next
            head = head.next
        
        return dummy.next
            
            
            
        
        
        