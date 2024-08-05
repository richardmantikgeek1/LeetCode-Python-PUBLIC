class Solution:
    def greatestLetter(self, s: str) -> str:
        memo = {}
        for c in s:
            memo[c] = True

        for A in range(90, 64, -1):
            if (chr(A) in memo.keys() and chr(A+32) in memo.keys()):
                return chr(A)
        return ''