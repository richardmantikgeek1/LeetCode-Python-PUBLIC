class Solution:
    def applyOperations(self, array):
        i = 0
        while (i < len(array)-1):
            if (array[i] == array[i+1]):
                array[i] *= 2
                array[i+1] = 0
            
            i += 1
        return [a for a in array if a > 0] + [a for a in array if a == 0]