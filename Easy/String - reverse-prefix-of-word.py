class Solution:
    def reversePrefix(self, word, c):
        i = word.find(c)
        if (i >= 0):
            word = word[i::-1] + word[i+1:]
        else:
            pass
        return word