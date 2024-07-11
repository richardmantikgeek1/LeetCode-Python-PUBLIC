from collections import deque 
class Solution:
    def plusOne(self, digits):
        carry = 0
        num_plus_one = deque([0] * len(digits))
        for i in range(len(digits) - 1, -1, -1):
            if (i == len(digits) - 1):
                d = digits[i] + 1 
            else:
                d = digits[i] + carry
            carry = d // 10
            num_plus_one[i] = d % 10

        if (carry > 0):
            num_plus_one.appendleft(carry)

        return list(num_plus_one)

digits = [9,9,9]
sol = Solution()
num_plus_one = sol.plusOne(digits)
print(num_plus_one)

