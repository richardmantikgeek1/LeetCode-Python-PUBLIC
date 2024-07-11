class Solution:
    def checkIfPangram(self, sentence):
        memo = {}
        start_index = 0
        while (start_index < len(sentence)):
            c = sentence[start_index]

            if (c in memo.keys()):
                memo[c] += 1
            else:
                memo[c] = 1

            start_index += 1
        
        return len(memo.keys()) == 26