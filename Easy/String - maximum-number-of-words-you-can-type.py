class Solution:
    def canBeTypedWords(self, text, brokenLetters):
        ret_val = 0
        words = text.split(' ')
        for word in words:
            can_be_typed = True
            for c in brokenLetters:
                if word.count(c) > 0:
                    can_be_typed = False
                    break
            if (can_be_typed):
                ret_val += 1
        
        return ret_val