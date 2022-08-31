class Solution:
    def get_neighbors(self, pos: int):
        neighbors = {
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [9,3, 0],
            5: [],
            6: [0, 7, 1],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        return neighbors[pos]
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        prev_nums = [1]*10
        cur_jump = 1
        while cur_jump < n:
            cur_nums = [0]*10
            cur_jump += 1
            for i in range(10):
                for pos in self.get_neighbors(i):
                    cur_nums[i] += prev_nums[pos]
            prev_nums = cur_nums
        print(cur_nums) 
        return sum(cur_nums) % (10**9 + 7)
        