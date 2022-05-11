class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        inc_stack = deque()
        inc_stack.append(-1)
        heights.append(0)
        max_area = 0
        for i, height in enumerate(heights):
            while heights[inc_stack[-1]] > height:
                h = heights[inc_stack.pop()]
                w = i - inc_stack[-1] - 1
                max_area = max(max_area, w*h)
            inc_stack.append(i)
        return max_area
            