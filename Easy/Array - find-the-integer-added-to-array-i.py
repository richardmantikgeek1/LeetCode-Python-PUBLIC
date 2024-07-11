class Solution:
    def addedInteger(self, array_1, array_2):
        array_1 = sorted(array_1)
        array_2 = sorted(array_2)
        
        return array_2[0]-array_1[0]
