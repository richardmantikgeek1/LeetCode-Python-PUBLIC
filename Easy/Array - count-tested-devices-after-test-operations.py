class Solution:
    def countTestedDevices(self, battery_percentages):
        ret_val = 0
        i = 0
        while (i < len(battery_percentages)):
            if (battery_percentages[i] > 0):
                ret_val += 1

                j = i + 1
                while (j < len(battery_percentages)):
                    battery_percentages[j] -= 1
                    j += 1
            else:
                pass
            i += 1 
        
        return ret_val