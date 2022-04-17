class Node:
    def __init__(self, val, key, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
        
        
        
class LRUCache:

    def __init__(self, capacity: int):
        self.node_pointers = {}
        self.head = Node(-1, -1)
        self.tail = Node(-2, -2, self.head, None)
        self.cap = capacity
        self.head.next = self.tail
        self.current_load = 0
        

    def get(self, key: int) -> int:
        if self.node_pointers.get(key):
            self.update_recency(key)
            return self.node_pointers[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.node_pointers.get(key):
            self.node_pointers[key].val = value
            self.update_recency(key)
        else:
            if self.current_load >= self.cap:
                self.evict_last_node()
            
            self.insert_node(key, value)
    
    def insert_node(self, key, value):
        # print(f'Inserting node {value}')
        self.current_load += 1
        next = self.head.next
        new_node = Node(value, key, self.head, next)
        self.node_pointers[key] = new_node
        self.head.next = new_node
        next.prev = new_node
        # print(f'New first node: {self.head.next.val}')
        # print(f'Prev node: {new_node.prev.val}')
        # print(f'Next node: {new_node.next.val}')

        
    
    def evict_last_node(self):
        
        last_node = self.tail.prev
        # print(f"Deleting {last_node.val}")
        new_last_node = last_node.prev
        # print(f'New last node {new_last_node.val}')
        self.tail.prev = new_last_node
        new_last_node.next = self.tail
        del self.node_pointers[last_node.key]
        # print(f'New last Node {self.tail.prev.val}')
        self.current_load -= 1
            
    def update_recency(self, key):
        cur_node = self.node_pointers[key]
        # print(f'Updating recency of {cur_node.val}')
        prev_node = cur_node.prev
        prev_node.next = cur_node.next
        cur_node.next.prev = prev_node
        
        next = self.head.next
        cur_node.next = next
        next.prev = cur_node
        cur_node.prev = self.head
        self.head.next = cur_node
        # print(f'New first node {self.head.next.val}')
        # print(f'Prev node: {cur_node.prev.val}')
        # print(f'Next node: {cur_node.next.val}')
        # print(f'New last node {self.tail.prev.val}')
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)