class Solution:
    def arrayRankTransform(self, array):
        rank_map = {}
        sorted_array = sorted(array)
        margin = 0
        for i in range(0, len(sorted_array)):
            num = sorted_array[i]
            if (num not in rank_map):
                rank_map[num] = i + 1 - margin
            else:
                margin += 1
        ret_val = []
        for i in range(0, len(array)):
            num = array[i]
            ret_val.append(rank_map[num])
        return ret_val