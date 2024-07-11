class Solution:
    def numberOfPairs(self, array_1, array_2, k):
        memo = {}
        ret_val = 0
        for i in range(0, len(array_1)):
            num_i = array_1[i]
            for j in range(0, len(array_2)):
                num_j = array_2[j]
                if (num_i % (num_j * k) == 0):
                    ret_val += 1
        return ret_val