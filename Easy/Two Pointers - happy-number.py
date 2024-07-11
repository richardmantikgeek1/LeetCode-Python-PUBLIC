class Solution:
    def isHappy(self, num):
        num_str = str(num)

        visited_sum_squares_digits = {}
        visited_sum_squares_digits[num] = True
        sum_squares_digits = self.sum_squares_digits(num)
        while (sum_squares_digits != 1):
            if (sum_squares_digits in visited_sum_squares_digits.keys()):
                return False
            visited_sum_squares_digits[sum_squares_digits] = True
            sum_squares_digits = self.sum_squares_digits(sum_squares_digits)

        return True

    def sum_squares_digits(self, num):
        num_str = str(num)
        ret_val = 0
        for i in range(0, len(num_str)):
            digit = int(num_str[i])
            ret_val += digit**2

        return ret_val

        


num = 19
sol = Solution()
print(sol.isHappy(num))