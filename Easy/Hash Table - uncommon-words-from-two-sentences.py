class Solution:
    def uncommonFromSentences(self, s1, s2):
        words_1 = s1.split(' ')
        words_2 = s2.split(' ')
        memo_1 = {}
        for word in words_1:
            if (word in memo_1.keys()):
                memo_1[word] += 1
            else:
                memo_1[word] = 1
        memo_2 = {}
        for word in words_2:
            if (word in memo_2.keys()):
                memo_2[word] += 1
            else:
                memo_2[word] = 1
        
        ret_val = []
        for word in memo_1.keys():
            if (memo_1[word] == 1 and word not in memo_2.keys()):
                ret_val.append(word)
        for word in memo_2.keys():
            if (memo_2[word] == 1 and word not in memo_1.keys()):
                ret_val.append(word)
        
        return ret_val