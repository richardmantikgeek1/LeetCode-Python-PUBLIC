class Solution:
    def buyChoco(self, prices, money) -> int:
        sorted_prices = sorted(prices)
        if (money >= sorted_prices[0] + sorted_prices[1]):
            return money - (sorted_prices[0] + sorted_prices[1])
        else:
            return money