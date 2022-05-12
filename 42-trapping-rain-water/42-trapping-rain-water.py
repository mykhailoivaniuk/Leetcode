class Solution:
    def trap(self, height: List[int]) -> int:
        decr_stack = deque()
        res = 0
        for i, cur_h in enumerate(height):
            while len(decr_stack) > 0 and decr_stack[-1][1] < cur_h:
                mid_idx, mid_h = decr_stack.pop()
                
                if decr_stack:
                    left_idx, left_h = decr_stack[-1]
                    res += (i - left_idx -1)*(min(cur_h, left_h)-mid_h)     
            decr_stack.append((i, cur_h))
        return res
            
        