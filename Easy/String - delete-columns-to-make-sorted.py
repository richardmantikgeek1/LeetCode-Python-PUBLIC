class Solution:
    def minDeletionSize(self, array):
        ret_val = 0
        i = len(array[0]) - 1
        while (i >= 0):
            last_c = None
            is_lexicographically_sorted = True
            for word in array:
                c = word[i]
                if (last_c is not None and c < last_c):
                    is_lexicographically_sorted = False
                last_c = c
            if (not is_lexicographically_sorted):
                ret_val += 1
            i -= 1
        
        return ret_val