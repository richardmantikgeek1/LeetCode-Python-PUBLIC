class Solution:
    def finalPrices(self, prices):
        ret_val = []
        for i in range(0, len(prices)):
            price_i = prices[i]
            discounted_price_i = None
            for j in range(i+1, len(prices)):
                price_j = prices[j]
                if (price_i >= price_j):
                    discounted_price_i = price_i - price_j
                    break
            if (discounted_price_i is not None):
                ret_val.append(discounted_price_i)
            else:
                ret_val.append(price_i)
        
        return ret_val        