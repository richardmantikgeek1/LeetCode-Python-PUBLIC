class Solution:
    def countPairs(self, array, k):
        ret_val = 0
        for i in range(0, len(array)):
            num_i = array[i]
            for j in range(i + 1, len(array)):
                num_j = array[j]
                if (num_i == num_j and (i * j) % k == 0):
                    ret_val += 1
                    
        return ret_val