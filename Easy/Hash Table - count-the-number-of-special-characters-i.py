class Solution:
    def numberOfSpecialChars(self, word):
        memo_lowercase = {}
        memo_uppercase = {}
        ret_val = 0
        for i in range(0, len(word)):
            c = word[i]
            if (ord('A') <= ord(c) <= ord('Z')):
                memo_uppercase[c.lower()] = True

            if (ord('a') <= ord(c) <= ord('z')):
                memo_lowercase[c] = True
        
        return len(set(memo_uppercase.keys()).intersection(set(memo_lowercase.keys())))