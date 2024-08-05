from collections import defaultdict

class Solution:
    def countVowelSubstrings(self, word):
        vowels_map = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
        left_index      = 0
        right_index     = 0
        
        char_to_freq_map = defaultdict(int)
        ret_val = 0

        len_word = len(word)
        while(left_index < len_word):
            while (right_index < len_word):
                c = word[right_index]
                right_index += 1
                
                if (c in vowels_map.keys()):
                    char_to_freq_map[c] += 1
                    print('a', char_to_freq_map)
                    input()
                    if (char_to_freq_map.keys() == vowels_map.keys()):
                        ret_val += 1
                else:
                    break

            if(left_index < len_word):
                c = word[left_index]
                print(left_index, c)
                left_index += 1
                if (c in vowels_map.keys()):
                    char_to_freq_map[c] -= 1
                    
                    if (char_to_freq_map[c] == 0):
                        char_to_freq_map.pop(c)
                    print('b', char_to_freq_map)
                    input()
                    if (char_to_freq_map.keys() == vowels_map.keys()):
                        ret_val += 1
                else:
                    pass

        return ret_val
    
sol = Solution()
result = sol.countVowelSubstrings('cuaieuouac')
print(result)