class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ret_val = []
        for c in candies:
            if (c + extraCandies >= max(candies)):
                ret_val.append(True)
            else:
                ret_val.append(False)

        return ret_val