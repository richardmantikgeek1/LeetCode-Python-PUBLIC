class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        memo = {}
        ret_val = -1
        for i in range(0, len(s)):
            c = s[i]
            if (c not in memo.keys()):
                memo[c] = i
            else:
                ret_val = max(ret_val, i - memo[c] - 1)
        
        return ret_val