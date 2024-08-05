class Solution:
    def divisorSubstrings(self, num, k):
        num_str = str(num)
        len_num_str = len(num_str)
        start_index = 0
        end_index = start_index + k - 1
        ret_val = 0
        while (end_index < len_num_str):
            d = int(num_str[start_index:end_index+1])
            if (d != 0 and num % d == 0):
                ret_val += 1
            start_index += 1
            end_index = start_index + k - 1

        return ret_val