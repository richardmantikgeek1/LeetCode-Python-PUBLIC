class Solution:
    def calculateTax(self, brackets, income):
        i = 0
        income_tax_payable = 0
        upper_i_min_1 = 0
        while (i < len(brackets) and income >= upper_i_min_1):
            upper_diff = None
            if (i > 0):
                upper_diff = brackets[i][0] - brackets[i-1][0]
            else:
                upper_diff = brackets[i][0]    
            if (income <= brackets[i][0]):
                income_tax_payable += (income - upper_i_min_1) * brackets[i][1] / 100
            elif (income > brackets[i][0]):
                income_tax_payable += upper_diff * brackets[i][1] / 100
            upper_i_min_1 = brackets[i][0]
            i += 1
                
        return income_tax_payable

brackets = [[1,0],[4,25],[5,50]]
income = 2
sol = Solution()
result = sol.calculateTax(brackets, income)
print(result)