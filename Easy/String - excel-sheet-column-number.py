class Solution:
    def titleToNumber(self, columnTitle):
        start_index = 0
        ret_val = 0
        while (start_index < len(columnTitle)):
            c = columnTitle[start_index]
            power = len(columnTitle) - start_index - 1
            col_num = (ord(c)-ord('A') + 1) * (26 ** power)
            ret_val += col_num
            start_index += 1

        return ret_val