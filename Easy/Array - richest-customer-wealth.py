class Solution:
    def maximumWealth(self, accounts):
        max_wealth = None
        for acc in accounts:
            sum_cust_savings = sum(acc)
            if (max_wealth is None or sum_cust_savings > max_wealth):
                max_wealth = sum_cust_savings

        return max_wealth
