class Solution:
    def countKDifference(self, array, k):
        memo = {}
        ret_val = 0
        for i in range(0, len(array)):
            num_i = array[i]
            if (num_i in memo.keys()):
                memo[num_i].append(i)
            else:
                memo[num_i] = [i]
        for j in range(0, len(array)):
            num_j = array[j]
            if (num_j + k in memo.keys()):
                ret_val += len([i for i in memo[num_j + k] if i < j])
            if (num_j - k in memo.keys()):
                ret_val += len([i for i in memo[num_j - k] if i < j])
        return ret_val
            