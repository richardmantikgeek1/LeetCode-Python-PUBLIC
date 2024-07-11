class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        i = 0
        while (i < len(words)):
            word = words[i]
            if (word == word[::-1]):
                return word
            i += 1
            
        return ''