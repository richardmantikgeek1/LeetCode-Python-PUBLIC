class Solution:
    def commonChars(self, words):
        first_word = words[0]
        char_found_index_map_array = []
        for w in range(0, len(words)):
            char_found_index_map_array.append({})
        
        ret_val = ''
        for c in first_word:
            is_char_shown_up_in_all_words = True
            for w in range(0, len(words)):
                word = words[w]
                if (c not in char_found_index_map_array[w].keys()):
                    i = word.find(c)
                    if (i < 0):
                        is_char_shown_up_in_all_words = False
                        break # !!!
                    char_found_index_map_array[w][c] = [i]
                else:
                    j = char_found_index_map_array[w][c][len(char_found_index_map_array[w][c]) - 1] + 1
                    if (j > 0):
                        while (j < len(word)):
                            if (word[j] == c):
                                char_found_index_map_array[w][c].append(j)
                                break
                            j += 1
                    else:
                        is_char_shown_up_in_all_words = False
                        break # !!!

                    if (j == len(word)):
                        is_char_shown_up_in_all_words = False
                        char_found_index_map_array[w][c].append(-1)
                        break # !!!
            if (is_char_shown_up_in_all_words):
                ret_val += c

        return ret_val