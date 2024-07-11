class Solution:
    def countGoodTriplets(self, array, a, b, c):
        ret_val = 0
        for i in range(0, len(array)):
            num_i = array[i]
            for j in range(i+1, len(array)):
                num_j = array[j]
                for k in range(j+1, len(array)):
                    num_k = array[k]
                    if (abs(num_i - num_j) <= a
                        and abs(num_j - num_k) <= b
                        and abs(num_i - num_k) <= c):
                        ret_val += 1

        return ret_val
                        