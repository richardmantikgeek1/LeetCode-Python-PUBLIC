class Solution:
    def maxProfit(self, prices):
        memo_buy = len(prices) * [0]
        memo_buy[0] = prices[0]
        memo_max_profit = len(prices) * [0]
        memo_max_profit[0] = prices[0] - memo_buy[0]
        i = 1
        while (i < len(prices)):
            memo_buy[i] = min (prices[i-1], memo_buy[i-1])
            memo_max_profit[i] = max(memo_max_profit[i-1], prices[i] - memo_buy[i])
            i += 1
        
        return memo_max_profit[i-1]