class Solution:
    def countBalls(self, low_limit, high_limit):
        memo = {}
        for num in range(low_limit, high_limit + 1):
            num_str = str(num)
            sum_digits = 0
            for i in range(0, len(num_str)):
                d = num_str[i]
                sum_digits += int(d)
            if (sum_digits in memo.keys()):
                memo[sum_digits] += 1
            else:
                memo[sum_digits] = 1
            
        return max(memo.values())
