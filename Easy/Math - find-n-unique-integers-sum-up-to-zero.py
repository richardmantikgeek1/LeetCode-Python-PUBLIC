class Solution:
    def sumZero(self, n):
        ret_val = []
        for a in range(1, n):
            ret_val.append(a)
        ret_val.append(-1 * sum(ret_val))

        return ret_val