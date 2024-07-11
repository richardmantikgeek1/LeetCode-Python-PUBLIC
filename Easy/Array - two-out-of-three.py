class Solution:
    def twoOutOfThree(self, array_1, array_2, array_3):
        map = {}
        for num in array_1 + array_2 + array_3:
            map[num] = True
        
        ret_val = []
        for k in map.keys():
            if ((k in array_1 and k in array_2) or
               (k in array_2 and k in array_3) or
               (k in array_1 and k in array_3)):
                ret_val.append(k)
    
        return ret_val