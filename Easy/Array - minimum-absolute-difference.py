class Solution:
    def minimumAbsDifference(self, array):
        array = sorted(array)
        min_abs_diff = None
        for i in range(0, len(array)-1):
            num_i = array[i]
            num_j = array[i+1]
            if (num_j > num_i):
                if (min_abs_diff is None or num_j - num_i < min_abs_diff):
                    min_abs_diff = num_j - num_i

        memo = {}
        for i in range(0, len(array) - 1):
            num_i = array[i]
            num_j = array[i+1]
            if (num_j > num_i and num_j - num_i == min_abs_diff):
                if (num_j - num_i in memo.keys()):
                    memo[num_j - num_i].append((num_i, num_j))
                else:
                    memo[num_j - num_i] = [(num_i, num_j)]
        
        return memo[min_abs_diff]