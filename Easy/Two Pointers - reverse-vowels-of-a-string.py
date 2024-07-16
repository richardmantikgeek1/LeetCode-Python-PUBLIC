class Solution:
    def reverseVowels(self, s):
        

        vowel_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        vowels = ''
        i = 0
        while (i < len(s)):
            c = s[i]
            if (c in vowel_chars):
                vowels += c
            i += 1
    
        i = 0
        vowels = vowels[::-1]
        j = 0
        
        ret_val = ''
        
        while (i < len(s)):
            c = s[i]
            if (c in vowel_chars):
                ret_val += vowels[j]
                j += 1
            else:
                ret_val += c
            i += 1 

        return ret_val