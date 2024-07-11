class Solution:
    def mergeSimilarItems(self, items_1, items_2):
        map = {}
        for i in range(0, len(items_1)):
            item_1 = items_1[i]
            map[item_1[0]] = item_1[1]
        
        for j in range(0, len(items_2)):
            item_2 = items_2[j]
            if (item_2[0] in map.keys()):
                map[item_2[0]] += item_2[1]
            else:
                map[item_2[0]] = item_2[1]
        
        ret_val = []
        for k in sorted(map.keys()):
            ret_val.append([k, map[k]])

        return ret_val