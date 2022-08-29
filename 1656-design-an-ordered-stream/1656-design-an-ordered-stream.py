class OrderedStream:

    def __init__(self, n: int):
        self.size = n
        self.idxs = [""]*n
        self.cur_idx = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.idxs[idKey - 1] = value
        if self.idxs[self.cur_idx] != "":
            while self.cur_idx < self.size and self.idxs[self.cur_idx] != "":
                res.append(self.idxs[self.cur_idx])
                self.cur_idx += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)