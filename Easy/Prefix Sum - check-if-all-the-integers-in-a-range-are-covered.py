import math
from collections import deque

class Solution:
    def isCovered(self, ranges, left, right) -> bool:
        start_num = min(r[0] for r in ranges)
        end_num = max(r[1] for r in ranges)

        if (start_num > right or end_num < left):
            return False

        for i in range(0, end_num - start_num + 1):
            b = False
            
            for j in range(0, len(ranges)):
                if (i + start_num >= ranges[j][0] and i + start_num <= ranges[j][1]):
                    b = True
            
            if (not b and i+start_num > left and i+start_num < right):
                return False

        return start_num <= left and end_num >= right