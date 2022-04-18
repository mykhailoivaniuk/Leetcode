class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = -1
        idx = len(heights) - 1
        while heights:
            cur_height = heights.pop()
            if cur_height > max_height:
                result.append(idx)
                max_height = cur_height
            idx -= 1
        result.reverse()
        return result
            
        