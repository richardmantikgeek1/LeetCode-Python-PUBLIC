class Solution:
    def minimumBoxes(self, apple, capacity):
        sum_apples = sum(apple)
        capacity = sorted(capacity, reverse = True)
        remainder = sum_apples
        i = 0
        ret_val = 0
        while(remainder > 0):
            remainder -= capacity[i]
            ret_val += 1
            i += 1
            
        return ret_val