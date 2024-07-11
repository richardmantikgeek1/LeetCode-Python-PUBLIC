class Solution:
    def maxRepeating(self, sequence, word):
        memo = word
        max_k = 0
        while (sequence.find(memo) != -1):
            max_k += 1
            memo = memo + word
        return max_k