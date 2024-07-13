class Solution:
    def similarPairs(self, words):
        memo = []
        for i in range(0, len(words)):
            word = words[i]
            memo.append({})
            for c in word:
                if (c in memo[i].keys()):
                    memo[i][c] += 1
                else:
                    memo[i][c] = 1
        
        ret_val = 0
        for i in range(0, len(memo)):
            for j in range(i+1, len(memo)):
                if (memo[i].keys() == memo[j].keys()):
                    ret_val += 1

        return ret_val
