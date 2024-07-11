class Solution:
    def vowelStrings(self, words, start_index, end_index):
        vowels = ['a', 'e', 'i', 'o', 'u']

        ret_val = 0
        for i in range(start_index, end_index + 1):
            word = words[i]
            if (word[0] in vowels and word[len(word)-1] in vowels):
                ret_val += 1
        
        return ret_val