class Solution:
    def repeatedNTimes(self, array):
        memo = {}
        for i in range(0, len(array)):
            num = array[i]
            if (num in memo.keys()):
                memo[num] += 1
            else:
                memo[num] = 1

        for k in memo.keys():
            if (memo[k] == len(array) // 2):
                return k

        return None