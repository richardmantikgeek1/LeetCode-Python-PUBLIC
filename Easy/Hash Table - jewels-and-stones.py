class Solution:
    def numJewelsInStones(self, jewels, stones):
        memo = {}
        for j in jewels:
            memo[j] = True

        ret_val = 0
        for s in stones:
            if (s in memo.keys()):
                ret_val += 1
        return ret_val