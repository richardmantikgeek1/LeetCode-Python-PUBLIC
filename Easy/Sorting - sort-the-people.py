class Solution:
    def sortPeople(self, names, heights):
        map = {}
        for i in range(0, len(heights)):
            height = heights[i]
            if (height in map.keys()):
                map[height].append(names[i])
            else:
                map[height] = [names[i]]
        
        ret_val = []
        for k in reversed(sorted(map.keys())):
            ret_val.extend(map[k])
        
        return ret_val