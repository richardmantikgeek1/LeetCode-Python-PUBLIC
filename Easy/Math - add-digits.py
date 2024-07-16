class Solution:
    def addDigits(self, num):
        
        while (len(str(num)) > 1):
            sum_digits = 0
            for c in str(num):
                sum_digits += int(c)
                num = sum_digits   
        
        return num
    
sol = Solution()
sol.addDigits(38)