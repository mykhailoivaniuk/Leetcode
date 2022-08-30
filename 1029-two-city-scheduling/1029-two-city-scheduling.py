class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        n = (len(costs) // 2) - 1
        res = 0
        for i in range(len(costs)):
            if i > n:
                res += costs[i][1]
            else:
                res += costs[i][0]
        return res