class Solution:
    def repeatedCharacter(self, s):
        memo = {}
        for i in range(0, len(s)):
            c = s[i]
            if (c in memo.keys()):
                return c
            memo[c] = True

        return None
