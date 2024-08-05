class Solution:
    def makeEqual(self, words):
        memo = {}
        
        for word in words:
            for c in word:
                if (c in memo.keys()):
                    memo[c] += 1
                else:
                    memo[c] = 1
        
        for c in memo.keys():
            if (memo[c] % len(words) != 0):
                return False

        return True