class Solution:
    def mergeAlternately(self, word_1, word_2):
        i = 0
        j = 0
        ret_val = ''
        step = 0
        while (i < len(word_1) and j < len(word_2)):
            if (step % 2 == 0):
                ret_val += word_1[i]
                i += 1
            else:
                ret_val += word_2[j]
                j += 1
            step += 1

        if (i < len(word_1)):
            ret_val += word_1[i:]

        if (j < len(word_2)):
            ret_val += word_2[j:]
        
        return ret_val

sol = Solution()
print(sol.mergeAlternately('ab', 'pqrs'))