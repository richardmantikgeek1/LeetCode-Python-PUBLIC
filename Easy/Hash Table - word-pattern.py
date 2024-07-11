class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if (len(pattern) != len(words)):
            return False

        pattern_to_word_map = {}
        word_to_pattern_map = {}

        for i in range(0, len(pattern)):
            c = pattern[i]
            word = words[i]
            if (c in pattern_to_word_map.keys() and pattern_to_word_map[c] != word):
                return False
            if (word in word_to_pattern_map.keys() and word_to_pattern_map[word] != c):
                return False

            pattern_to_word_map[c] = word
            word_to_pattern_map[word] = c

        return True