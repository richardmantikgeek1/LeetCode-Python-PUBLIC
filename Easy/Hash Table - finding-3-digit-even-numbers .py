from collections import defaultdict

class Solution:
    def findEvenNumbers(self, digits):
        ret_val = defaultdict(bool)
        for num in range(100, 1000):
            if (num % 2 == 0):
                is_appended = True
                int_digits = list(str(num))
                for d in range(0, 10):
                    if int_digits.count(str(d)) > digits.count(d):
                        is_appended = False
                if (is_appended):
                    ret_val[num] = True
        
        return sorted(ret_val.keys())

digits = [2,1,3,0]
sol = Solution()
sol.findEvenNumbers(digits)