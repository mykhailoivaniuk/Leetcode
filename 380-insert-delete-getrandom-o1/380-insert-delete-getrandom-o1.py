class RandomizedSet:

    def __init__(self):
        self.ids = []
        self.values = {}

    def insert(self, val: int) -> bool:
        if self.values.get(val) is not None:
            return False
        self.values[val] = len(self.ids)
        self.ids.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if self.values.get(val) is None:
            return False
        delete_idx = self.values[val]
        last_elem_idx = self.values[self.ids[-1]]
        self.values[self.ids[-1]] = delete_idx
        self.ids[delete_idx], self.ids[-1] = self.ids[-1], self.ids[delete_idx]
        
        self.ids.pop()
        del self.values[val]
        return True
    
    def getRandom(self) -> int:
        return random.choice(self.ids)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()