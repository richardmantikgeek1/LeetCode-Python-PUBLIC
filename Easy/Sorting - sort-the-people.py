class Solution:
    def sortPeople(self, names, heights):
        height_to_names_map = {}
        for i in range(0, len(names)):
            name = names[i]
            height = heights[i]
            if (height in height_to_names_map.keys()):
                height_to_names_map[height].append(name)
            else:
                height_to_names_map[height] = [name]

        ret_val = []
        for height in reversed(sorted(height_to_names_map.keys())):
            ret_val.extend(height_to_names_map[height])
        
        return ret_val

        