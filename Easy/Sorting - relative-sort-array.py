class Solution:
    def relativeSortArray(self, array_1, array_2):
        map = {}
        # map[2] = 3
        # map[1] = 1
        # map[4] = 4
        for i in range(0, len(array_1)):
            num = array_1[i]
            if (num in map.keys()):
                map[num] += 1
            else:
                map[num] = 1
        
        ret_val = []
        for i in range(0, len(array_2)):
            num = array_2[i]
            #map[num] -= 1
            #if (map[num] == 0):
            #    map.pop(num)
            ret_val.extend([num] * map[num])

        for num in sorted(array_1):
            if (num not in array_2):
                ret_val.append(num)

        return ret_val