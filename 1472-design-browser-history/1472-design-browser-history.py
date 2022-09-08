class Node:
    def __init__(self, val: str, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next
        

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur_node = Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = Node(url)
        self.cur_node.next = None
        new_node.prev = self.cur_node
        self.cur_node.next = new_node
        self.cur_node = new_node

    def back(self, steps: int) -> str:
        while self.cur_node.prev is not None and steps > 0:
            steps -= 1
            self.cur_node = self.cur_node.prev
        return self.cur_node.val

    def forward(self, steps: int) -> str:
        while self.cur_node.next is not None and steps > 0:
            self.cur_node = self.cur_node.next
            steps -= 1
        return self.cur_node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)