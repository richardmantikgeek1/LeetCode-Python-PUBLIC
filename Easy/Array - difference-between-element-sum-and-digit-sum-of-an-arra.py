class Solution:
    def differenceOfSum(self, array):
        sum_elements = sum(array)
        sum_digits = 0
        for num in array:
            sum_digits += sum([int(d) for d in str(num)])
        
        return sum_elements - sum_digits