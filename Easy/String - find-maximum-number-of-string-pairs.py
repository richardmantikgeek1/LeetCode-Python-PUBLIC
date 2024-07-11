class Solution:
    def maximumNumberOfStringPairs(self, words):
        memo = {}
        for i in range(0, len(words)):
            word = words[i]
            if (word in memo.keys()):
                pass
            elif (word[::-1] in memo.keys()):
                word = word[::-1]

            if (word in memo.keys()):
                memo[word] += 1
            else:
                memo[word] = 1
        
        ret_val = 0
        for k in memo.keys():
            if (memo[k] >= 2):
                ret_val += 1
        
        return ret_val
