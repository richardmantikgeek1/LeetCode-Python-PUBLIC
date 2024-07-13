class Solution:
    def countWords(self, words_1, words_2):
        memo_words_1 = {}
        for word in words_1:
            if (word in memo_words_1.keys()):
                memo_words_1[word] += 1
            else:
                memo_words_1[word] = 1
        memo_words_2 = {}
        for word in words_2:
            if (word in memo_words_2.keys()):
                memo_words_2[word] += 1
            else:
                memo_words_2[word] = 1
        
        intersect_words = set(memo_words_1.keys()).intersection(set(memo_words_2.keys()))
        ret_val = 0
        for word in intersect_words:
            if (memo_words_1[word] == 1 and memo_words_2[word] == 1):
                ret_val += 1

        return ret_val