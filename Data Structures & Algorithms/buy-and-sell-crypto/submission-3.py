class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0               
        r = l+1
        while r < len(prices): # is the same as r <= len(prices) -1 but this is cleaner
            if prices[l] < prices[r]: #cleaner way to handle the loops rather than [l] > [r], but logic is the same
                profit = prices[r] - prices[l] #don't need to initialize before, profit only lives here
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1      #had this in both arms of if-else, that was redundant if it happens every iteration
        return max_profit