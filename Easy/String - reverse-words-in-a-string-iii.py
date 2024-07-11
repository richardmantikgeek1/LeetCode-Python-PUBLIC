class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ret_val = []
        i = 0
        while (i < len(words)):
            ret_val.append(words[i][::-1])
            i += 1
        return ' '.join(ret_val)