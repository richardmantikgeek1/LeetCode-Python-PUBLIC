class Solution:
    def kthDistinct(self, array, k):
        memo = {}
        for i in range(0, len(array)):
            word = array[i]
            if (word in memo.keys()):
                memo[word] += 1
            else:
                memo[word] = 1

        i = 0    
        for word in memo.keys():
            if (memo[word] > 1):
                continue
            if (i + 1 == k):
                return word
            i += 1

        return ''