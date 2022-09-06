class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min = prices[0]
        diff = 0
        for i in range(len(prices)):
            if prices[i]< last_min:
                last_min = prices[i]
            diff = max(diff, prices[i] - last_min)
        
        return diff
        