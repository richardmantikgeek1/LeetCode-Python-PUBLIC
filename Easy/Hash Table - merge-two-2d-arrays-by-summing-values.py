class Solution:
    def mergeArrays(self, array_1, array_2):
        a_map = {}
        for pair in array_1:
            key = pair[0]
            val = pair[1]
            a_map[key] = val
        for pair in array_2:
            key = pair[0]
            val = pair[1]
            if (key in a_map.keys()):
                a_map[key] = val + a_map[key]
            else:
                a_map[key] = val
        ret_val = []
        for k in sorted(a_map.keys()):
            ret_val.append([k, a_map[k]])
        return ret_val