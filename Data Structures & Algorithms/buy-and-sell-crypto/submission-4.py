class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        best_profit = 0

        for day in range(1,len(prices)):
            min_buy = min(min_buy, prices[day])
            best_profit = max(best_profit, (prices[day] - min_buy))
        return best_profit