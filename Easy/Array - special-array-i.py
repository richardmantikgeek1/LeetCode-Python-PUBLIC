class Solution:
    def isArraySpecial(self, array):
        i = 0
        while (i < len(array)-1):
            if (array[i] % 2 == array[i+1] % 2):
                return False
            i += 1
            
        return True