class Solution:
    def findWords(self, words):
        first_row_chars = 'qwertyuiop'
        second_row_chars = 'asdfghjkl'
        third_row_chars = 'zxcvbnm'
        
        first_row_map = {}
        for frc in first_row_chars:
            first_row_map[frc] = True
        
        second_row_map = {}
        for src in second_row_chars:
            second_row_map[src] = True

        third_row_map = {}
        for src in third_row_chars:
            third_row_map[src] = True

        memo = []
        memo.append(first_row_map)
        memo.append(second_row_map)
        memo.append(third_row_map)

        ret_val = []
        for word in words:
            for row_map in memo:
                print(word, row_map)
                if (self.is_word_typable_using_one_row_keyboard(word, row_map)):
                    ret_val.append(word)

        return ret_val
            
    def is_word_typable_using_one_row_keyboard(self, word, row_map):
        for c in word:
            if (c.lower() not in row_map.keys()):
                return False
            
        return True

sol = Solution()
sol.findWords([])