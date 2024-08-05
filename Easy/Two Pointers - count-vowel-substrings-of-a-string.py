class Solution:
    def countVowelSubstrings(self, word):
        vowels_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        memo = {}
        ret_val = 0
        len_substr = len(word)
        while (len_substr > 1):
            start_index = 0
            end_index = start_index + len_substr - 1
            while (end_index < len(word)):
                memo = {}
                for i in range(start_index, end_index+1):
                    c = word[i]
                    memo[c] = True
                if (memo == vowels_map):
                    ret_val += 1
                
                start_index += 1
                end_index = start_index + len_substr - 1

            len_substr -= 1

        return ret_val

sol = Solution()
result = sol.countVowelSubstrings('cuaieuouac')
print(result)