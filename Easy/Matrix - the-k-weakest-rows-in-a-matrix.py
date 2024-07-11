class Solution:
    def kWeakestRows(self, matrix, k):
        a_map = {}
        for i in range(0, len(matrix)):
            count_ones = matrix[i].count(1)
            if (count_ones in a_map.keys()):
                a_map[count_ones].append(i)
            else:
                a_map[count_ones] = [i]
        
        print(a_map)
        ret_val = []
        for key in sorted(a_map.keys()):
            if (len(a_map[key]) <= k):
                ret_val.extend(a_map[key])
                k = k - len(a_map[key])
            else:
                ret_val.extend(a_map[key][0:k])
                k = 0
            print(k)
            if (k == 0):
                break
        
        return ret_val
        