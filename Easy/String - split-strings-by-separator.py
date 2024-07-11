class Solution:
    def splitWordsBySeparator(self, words, separator):
        ret_val = []
        for word in words:
            ret_val.extend([w for w in word.split(separator) if w != ''])
        
        return ret_val