class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        l = 0
        r = l+1
        while r <= len(prices) -1:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
        return max_profit