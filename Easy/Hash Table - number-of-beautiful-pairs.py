import math
from collections import defaultdict

class Solution:
    def countBeautifulPairs(self, array):
        ret_val = 0
        first_digit_to_indices_map = defaultdict(list)
        for i in range(0, len(array)):
            num_i = array[i]
            num_i_str = str(num_i)
            first_digit_i = int(num_i_str[0])
            first_digit_to_indices_map[first_digit_i].append(i)
        
        last_digits_to_indices_map = defaultdict(list)
        for j in range(0, len(array)):
            num_j = array[j]
            num_j_str = str(num_j)
            last_digit_j = int(num_j_str[len(num_j_str) - 1])
            last_digits_to_indices_map[last_digit_j].append(j)
    
        ret_val = 0
        for x in first_digit_to_indices_map.keys():
            i_indices = first_digit_to_indices_map[x]
            for y in last_digits_to_indices_map.keys():
                j_indices = last_digits_to_indices_map[y]
                if (math.gcd(x, y) == 1):
                    ret_val += len([(i, j) for i in i_indices for j in j_indices if i < j])
                    
        return ret_val
                    

array = [2,5,1,4]
sol = Solution()
result = sol.countBeautifulPairs(array)
print(result)