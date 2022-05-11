class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        cur_max = 0
        prev_row = None
        cur_row = None
        decode = {"0":0, "1":1}
        max_area = 0
        for i in range(len(matrix)):
            cur_row = [decode[i] for i in matrix[i]]
            cur_row.append(0)
            if prev_row:
                for j in range(len(prev_row)):
                    if cur_row[j] != 0:
                        cur_row[j] += prev_row[j]
                max_area = self.findLR1D(cur_row, max_area)
                prev_row = cur_row
                    
            else:
                max_area = self.findLR1D(cur_row, max_area)
                prev_row = cur_row
        
        return max_area
    
    
    def findLR1D(self, row: List[int], max_area):
        
        inc_stack = deque()
        inc_stack.append(-1)
        for i, height in enumerate(row):
            while row[inc_stack[-1]] > height:
                h = row[inc_stack.pop()]
                w = i - inc_stack[-1] -1
                max_area = max(max_area, h*w)
            inc_stack.append(i)
        return max_area
        
        