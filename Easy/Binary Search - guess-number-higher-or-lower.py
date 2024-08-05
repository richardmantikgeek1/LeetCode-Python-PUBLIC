# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        start_index = 1
        end_index = n

        return self.guess_number(n, start_index, end_index)

    def guess_number(self, n, start_num, end_num):
        mid_num = (start_num + end_num) // 2
        
        if (guess(mid_num) == 0):
            return mid_num
        elif (guess(mid_num) < 0):
            return self.guess_number(n, 1, mid_num - 1)
        else:
            return self.guess_number(n, mid_num + 1, end_num)
        