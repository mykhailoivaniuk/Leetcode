class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res = [0] * len(temps)
        s = deque()  
        for i, temp in enumerate(temps):
            while s and temp > s[-1][1]:
                idx, val = s.pop()
                res[idx] = i - idx
            s.append((i, temp))
        
        return res
                
                

        