class Solution:
    def unequalTriplets(self, array):
        ret_val = 0
        for i in range(0, len(array)):
            for j in range(i+1, len(array)):
                for k in range(j+1, len(array)):
                    if(array[i]!= array[j] 
                       and array[j] != array[k] 
                       and array[i] != array[k]):
                        ret_val += 1
                        
        return ret_val