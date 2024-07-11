class Solution:
    def targetIndices(self, array, target):
        array = sorted(array)
        ret_val = []
        try:
            i = array.index(target)
        except:
            return []
        
        while (i < len(array)):
            if (array[i] == target):
                ret_val.append(i)
            i += 1

        return ret_val