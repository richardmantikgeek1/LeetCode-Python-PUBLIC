class Solution:
    def findFinalValue(self, array, original_num) -> int:
        memo = {}
        for i in range(0, len(array)):
            num = array[i]

            memo[num] = True
        
        while (original_num in memo.keys()):
            original_num = original_num * 2
        
        return original_num
