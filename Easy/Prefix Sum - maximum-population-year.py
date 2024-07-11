import math
from collections import deque
class Solution:
    def maximumPopulation(self, logs):
        start_year = min(l[0] for l in logs)
        end_year = max(l[1] for l in logs)
        
        left_sum    = deque()
        right_sum   = deque()
        prefix_sum  = 0

        for i in range(0, end_year - start_year + 1):
            for j in range(0, len(logs)):
                if (logs[j][0] == i + start_year):
                    prefix_sum += 1
                if (logs[j][1] == i + start_year):
                    prefix_sum -= 1
            left_sum.append(prefix_sum)

        max_population = max(left_sum)
        max_population_index = left_sum.index(max_population)

        return start_year + max_population_index
    
array = [[1993,1999],[2000,2010]]
sol = Solution()
max_population = sol.maximumPopulation(array)
print(max_population)