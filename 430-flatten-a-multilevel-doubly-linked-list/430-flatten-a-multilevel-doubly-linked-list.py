"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
from collections import deque
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return head
        dummy = Node(0)
        stack = deque()
        stack.append(head)
        cur = dummy
        while stack:
            tmp = stack.pop()
            if tmp.next: stack.append(tmp.next)
            if tmp.child: stack.append(tmp.child)
            cur.next = tmp
            tmp.prev = cur
            tmp.child = None
            cur = cur.next
        dummy.next.prev = None
        return dummy.next
            
            
        