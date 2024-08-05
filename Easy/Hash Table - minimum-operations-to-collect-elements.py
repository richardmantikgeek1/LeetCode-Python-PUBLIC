from collections import defaultdict

class Solution:
    def minOperations(self, array, k):
        removed_nums_map = defaultdict(bool)
        ret_val = 0
        for i in range(len(array) - 1, -1, -1):
            ret_val += 1
            num = array[i]
            removed_nums_map[num] = True
            if (set(range(1,k+1)).issubset(set(removed_nums_map.keys()))):
                return ret_val
        
        return ret_val
