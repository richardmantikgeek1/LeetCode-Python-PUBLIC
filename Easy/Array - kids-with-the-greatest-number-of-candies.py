class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ret_val = []
        for i in range(0, len(candies)):
            candies_copy = candies.copy()
            candies_copy[i] += extraCandies
            ret_val.append(candies_copy[i] >= max(candies))
            
        return ret_val