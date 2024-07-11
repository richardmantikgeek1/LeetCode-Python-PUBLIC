class Solution:
    def countCompleteDayPairs(self, hours):
        ret_val = 0
        for i in range(0, len(hours)):
            for j in range(i+1, len(hours)):
                if ((hours[i] + hours[j]) % 24 == 0):
                    ret_val += 1
        
        return ret_val