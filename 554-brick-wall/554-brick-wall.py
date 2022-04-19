class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cur_min = float('inf')
        
        block_ends = {}
        height = len(wall)
        width = sum(wall[0])
        for i in range(len(wall)):
            cur_width = 0
            for j in range(len(wall[i])):
                cur_width += wall[i][j]
                block_ends[cur_width] = block_ends.get(cur_width, 0) + 1
                if cur_width != width:
                    cur_min = min(cur_min, height - block_ends[cur_width])
        
        if cur_min == float('inf'):
            return height
        return cur_min
        
        