class Solution:
    def truncateSentence(self, sentence, k):
        return ' '.join(sentence.split(' ')[:k])