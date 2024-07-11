class Solution:
    def numberOfPoints(self, array):
        map = {}
        for start_coord, end_coord in array:
            if (start_coord in map.keys()):
                map[start_coord] += 1
            else:
                map[start_coord] = 1
            if (end_coord in map.keys()):
                map[end_coord] += 1
            else:
                map[end_coord] = 1

        ret_val = 0
        for coord in range(min(map.keys()), max(map.keys())+1):
            is_intersects = False
            for start_coord, end_coord in array:
                if (start_coord <= coord <= end_coord):
                    is_intersects = True
            if (is_intersects):
                ret_val += 1
        
        return ret_val