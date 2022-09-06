from collections.abc import Callable

class Solution:
    def next_dir(self, prev: str) -> str:
        if prev == "left":
            return "up"
        if prev == "down":
            return "left"
        if prev == "up":
            return "right"
        if prev == "right":
            return "down"
        else:
            raise Exception(f"Unknown direction {prev}")
            
    def next_move(self, dirc: str, x: int, y: int) -> tuple[int, int]:
        if dirc == "left":
            return x - 1, y
        if dirc == "down":
            return x, y + 1
        if dirc == "up":
            return x, y - 1
        if dirc == "right":
            return x + 1, y
        else:
            raise Exception(f"Unknown direction {dirc}")
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length_moves = len(matrix[0])
        height_moves = len(matrix)
        cur_dir = "right"
        move_count = len(matrix)*len(matrix[0]) - 1
        res = [matrix[0][0]]
        x, y = 0, 0
        while move_count != 0:
            if cur_dir == "left" or cur_dir == "right":
                height_moves -= 1
                for i in range(length_moves):
                    x, y = self.next_move(cur_dir, x, y)
                    if x >= len(matrix[0]):
                        x -= 1
                        break
                    res.append(matrix[y][x])
                    move_count -= 1
                cur_dir = self.next_dir(cur_dir)
            else:
                length_moves -= 1
                for i in range(height_moves):
                    x, y = self.next_move(cur_dir, x, y)
                    if y >= len(matrix):
                        y -= 1
                        break
                    res.append(matrix[y][x])
                    move_count -= 1
                cur_dir = self.next_dir(cur_dir)
        
        return res
            
        
        
        
        
        