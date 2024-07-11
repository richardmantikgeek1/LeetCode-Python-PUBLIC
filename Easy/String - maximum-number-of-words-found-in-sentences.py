class Solution:
    def mostWordsFound(self, sentences):
        max_count_words = None
        for sentence in sentences:
            words = sentence.split(' ')
            count_words = len(words)
            if (max_count_words is None or max_count_words < count_words):
                max_count_words = count_words
        
        return max_count_words