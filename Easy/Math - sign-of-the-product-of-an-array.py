class Solution:
    def arraySign(self, array):
        count_neg_nums = 0
        count_zero_nums = 0
        count_pos_nums = 0

        for i in range(0, len(array)):
            num = array[i]
            if (num < 0):
                count_neg_nums += 1
            elif (num == 0):
                count_zero_nums += 1
            else:
                count_pos_nums += 1
        
        if (count_zero_nums > 0):
            return 0
        elif (count_neg_nums % 2 == 1):
            return -1
        else:
            return 1