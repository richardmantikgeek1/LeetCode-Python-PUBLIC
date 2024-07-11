class Solution:
    def kItemsWithMaximumSum(self, count_ones, count_zeros, count_neg_ones, k):
        items = [1] * count_ones + [0] * count_zeros + [-1] * count_neg_ones
        i = 0
        ret_val = 0
        while (i < k):
            ret_val += items[i]
            i += 1

        return ret_val