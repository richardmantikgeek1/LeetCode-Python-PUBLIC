class Solution:
    def distinctDifferenceArray(self, array):
        ret_val = []
        memo_suffix = {}
        for i in range(0, len(array)):
            if (array[i] in memo_suffix.keys()):
                memo_suffix[array[i]] += 1
            else:
                memo_suffix[array[i]] = 1
        
        memo_prefix = {}

        for i in range(0, len(array)):
            if (array[i] in memo_prefix.keys()):
                memo_prefix[array[i]] += 1
            else:
                memo_prefix[array[i]] = 1

            memo_suffix[array[i]] -= 1
            if (memo_suffix[array[i]] == 0):
                memo_suffix.pop(array[i])

            ret_val.append(len(memo_prefix.keys()) - len(memo_suffix.keys()))

        return ret_val