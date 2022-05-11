class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        next_smaller = [size - i for i in range(size)]
        prev_smaller = [i+1 for i in range(size)]
        mono_stack = deque()
        for i, height in enumerate(heights):
            while len(mono_stack) != 0 and heights[mono_stack[-1]] >= height:
                idx = mono_stack.pop()
                next_smaller[idx] = i - idx
            mono_stack.append(i)
        mono_stack.clear()
        for i in range(size - 1, -1, -1):
            while len(mono_stack) != 0 and heights[mono_stack[-1]] > heights[i]:
                idx = mono_stack.pop()
                prev_smaller[idx] = idx - i
            mono_stack.append(i)
        cur_max = 0
        for i, dist in enumerate(next_smaller):
                cur_max = max(cur_max, heights[i]*(next_smaller[i]+prev_smaller[i]-1))
        return cur_max
            
            
            
        