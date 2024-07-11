import math
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ret_val = ''
        while (columnNumber > 0):
            columnNumber -= 1
            p = columnNumber // 26
            r = columnNumber % 26
            ret_val = chr(65 + r) + ret_val
            columnNumber = p
        
        return ret_val