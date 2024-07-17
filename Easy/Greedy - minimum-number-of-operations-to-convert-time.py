class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_time = current.split(':')
        current_minutes = 60 * int(current_time[0]) + int(current_time[1])
        correct_time = correct.split(':')
        correct_minutes = 60 * int(correct_time[0]) + int(correct_time[1])

        time_inc = [60, 15, 5, 1]
        remainder = correct_minutes - current_minutes
        print(remainder)
        ret_val = 0
        while (remainder > 0):
            j = 0
            while (j < len(time_inc)):
                if (remainder >= time_inc[j]):
                    remainder = remainder - time_inc[j]
                    ret_val += 1
                else:
                    j += 1
        
        return ret_val
    
sol = Solution()
result = sol.convertTime('02:30', '04:35')
print(result)