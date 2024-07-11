class Solution:
    def findWordsContaining(self, words, c):
        ret_val = []
        for i in range(0, len(words)):
            j = words[i].find(c)
            if (j >= 0):
                ret_val.append(i)
        return ret_val