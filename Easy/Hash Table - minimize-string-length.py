class Solution:
    def minimizedStringLength(self, s):
        memo = {}
        for i in range(0, len(s)):
            c = s[i]
            memo[c] = True

        return len(memo.keys())